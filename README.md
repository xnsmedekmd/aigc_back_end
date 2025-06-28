# 古典文学小程序后端

这是一个基于Django和Django REST Framework的古典文学小程序后端项目，提供古诗和古文内容的API接口。

## 功能特性

- 提供古诗和古文的内容获取接口
- 支持视频内容和详细文本内容的获取
- 提供内容列表获取接口

## 技术栈

- Python 3.8+
- Django 4.2+
- Django REST Framework
- SQLite (开发环境)

## 安装说明

1. 克隆项目到本地

```bash
git clone <项目地址>
cd project
```

2. 安装依赖

```bash
pip install django djangorestframework
```

3. 初始化数据库

```bash
python manage.py migrate
```

4. 加载示例数据

```bash
python manage.py load_sample_data
```

5. 创建管理员用户

```bash
python manage.py createsuperuser
```

## 运行项目

```bash
python manage.py runserver 0.0.0.0:8000
```

## API接口

详细API接口文档可在 `api_document.md` 中查看。

主要接口包括：

- `/api/content/video` - 获取内容视频
- `/api/content/detail` - 获取内容详情
- `/api/content/list` - 获取所有内容列表

## 项目结构

```
project/
├── classical_literature/      # 古典文学应用
│   ├── management/           # 管理命令
│   ├── migrations/           # 数据库迁移文件
│   ├── static/               # 静态文件
│   │   ├── videos/           # 视频文件
│   │   └── images/           # 图片文件
│   ├── models.py             # 数据模型
│   ├── serializers.py        # 序列化器
│   ├── urls.py               # URL配置
│   └── views.py              # 视图函数
├── project/                   # 项目配置
├── api_document.md            # API文档
└── manage.py                  # Django管理脚本
```

## 示例请求

### 获取内容视频

```javascript
// 前端小程序请求示例
wx.request({
  url: 'https://your-domain.com/api/content/video',
  data: {
    type: 'poetry',
    id: 1
  },
  success(res) {
    console.log(res.data)
  }
})
```

## 注意事项

- 项目中的视频和图片资源需要自行上传到对应目录
- 生产环境部署时，请修改settings.py中的相关配置，关闭DEBUG模式
- 请妥善保管SECRET_KEY，不要泄露 