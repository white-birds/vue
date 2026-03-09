import jwt
import sys
from flask import request, redirect
from flask_login import login_user
from flask_appbuilder.security.manager import AUTH_DB
from superset.security import SupersetSecurityManager
from flask_appbuilder.security.views import AuthDBView
from flask_appbuilder import expose
from superset.utils.log import StdOutEventLogger

# ==========================================================
# 1. 基础与安全配置
# ==========================================================
SECRET_KEY = "sunhaoyuan421123"
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:123456@host.docker.internal:3306/superset'
WTF_CSRF_ENABLED = False
TALISMAN_ENABLED = False # 彻底解决 Iframe 里的白屏问题
HTTP_HEADERS = {"X-Frame-Options": "ALLOWALL"}

# ==========================================================
# 2. 权限隔离配置 (关键！)
# ==========================================================
# 核心：SSO 进来的用户给 Alpha，Alpha 可以编辑【自己】的图表，但不能改别人的
# 不要给 Admin，Admin 能看到并修改全系统所有人的图表！
AUTH_USER_REGISTRATION_ROLE = "Alpha" 
AUTH_USER_REGISTRATION = True

# 核心：设置游客角色为 Public，并让 Public 像 Gamma 一样（只能看，不能改）
PUBLIC_ROLE_LIKE = "Gamma" 
GUEST_ROLE_NAME = "Public"

# ==========================================================
# 3. Logo Configuration
# ==========================================================
# 自定义应用名称和图标
APP_NAME = "AI·HOM"
# 直接替换Superset的logo文件路径
LOGO_TARGET_PATH = "/static/assets/images/aihom-logo.png"
# 或者使用完整的品牌配置
APP_ICON = "/static/assets/images/aihom-logo.png"
# 设置favicon
FAVICONS = [{"href": "/static/assets/images/aihom-logo.png"}]

# ==========================================================
# 4. Language & Cookie Configuration
# ==========================================================
BABEL_DEFAULT_LOCALE = "zh"
# 只保留中文，隐藏语言选择器
LANGUAGES = {
    "zh": {"flag": "cn", "name": "中文"}
}
# Feature flags
FEATURE_FLAGS = {
    "EMBEDDED_SUPERSET": True, 
    "DASHBOARD_RBAC": True,
    "ENABLE_TEMPLATE_PROCESSING": True
}
SESSION_COOKIE_SAMESITE = 'Lax'
SESSION_COOKIE_SECURE = False
SESSION_COOKIE_HTTPONLY = True

# ==========================================================
# 4. SSO 免密登录逻辑 (改用 /sso/ 路由)
# ==========================================================
class CustomAuthView(AuthDBView):
    @expose('/sso/', methods=['GET', 'POST'])
    def sso_login(self):
        token = request.args.get('token')
        next_url = request.args.get('next', '/superset/welcome/')
        
        if token:
            try:
                SSO_SECRET = "aihom_superset_secret_key_2026"
                payload = jwt.decode(token, SSO_SECRET, algorithms=['HS256'])
                username = payload.get('username')
                
                if username:
                    sm = self.appbuilder.sm
                    user = sm.find_user(username=username)
                    if not user:
                        # 自动创建用户，初始角色为 Alpha
                        role = sm.find_role("Alpha")
                        user = sm.add_user(username, username, 'User', f'{username}@aihom.com', role, 'sso_pwd')
                        print(f"DEBUG_SSO: 创建 Alpha 用户: {username}", file=sys.stderr, flush=True)
                    
                    login_user(user, remember=True)
                    print(f"DEBUG_SSO: 用户 {username} 登录成功", file=sys.stderr, flush=True)
                    return redirect(next_url)
            except Exception as e:
                print(f"DEBUG_SSO: 异常 {str(e)}", file=sys.stderr, flush=True)
                
        return redirect('/login/')

class CustomSecurityManager(SupersetSecurityManager):
    def __init__(self, appbuilder):
        super(CustomSecurityManager, self).__init__(appbuilder)
        self.authdbview = CustomAuthView

CUSTOM_SECURITY_MANAGER = CustomSecurityManager

# ==========================================================
# 5. 特性开关
# ==========================================================
# 已在语言配置部分定义
RECAPTCHA_PUBLIC_KEY = ''
RECAPTCHA_PRIVATE_KEY = ''
EVENT_LOGGER = StdOutEventLogger()

# ==========================================================
# 6. 缓存与性能配置
# ==========================================================
# 禁用缓存 - 用于测试性能对比
CACHE_CONFIG = {
    'CACHE_TYPE': 'NullCache',  # 完全禁用缓存
    'CACHE_NO_NULL_WARNING': True
}

# Webserver 超时设置
SUPERSET_WEBSERVER_TIMEOUT = 300

# ==========================================================
# 7. Guest Token 配置 (用于嵌入式仪表板)
# ==========================================================
GUEST_TOKEN_JWT_SECRET = "sunhaoyuan421123"
GUEST_TOKEN_JWT_ALGO = "HS256"
GUEST_TOKEN_HEADER_NAME = "X-GuestToken"
GUEST_TOKEN_JWT_EXP_SECONDS = 300

# ==========================================================
# 8. CORS 配置 (允许跨域访问)
# ==========================================================
ENABLE_CORS = True
CORS_OPTIONS = {
    'supports_credentials': True,
    'allow_headers': ['*'],
    'resources': ['*'],
    'origins': ['*']
}