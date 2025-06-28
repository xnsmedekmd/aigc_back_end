# 古典文学小程序接口文档

## 概述

本文档描述了古典文学小程序前端与后端交互的API接口及其数据格式。小程序分为古诗与古文两个栏目，用户可以点击不同的内容项请求对应的视频或文本内容。

## 数据接口

### 1. 获取内容视频

**接口描述**: 请求指定分类和ID的内容视频

**请求方法**: `GET`

**接口URL**: `/api/content/video`

**请求参数**:

| 参数名 | 类型   | 是否必须 | 描述                                 |
| ------ | ------ | -------- | ------------------------------------ |
| type   | string | 是       | 内容类型，取值为 `poetry` 或 `prose` |
| id     | number | 是       | 内容ID                               |

**请求示例**:
```javascript
wx.request({
  url: 'https://api.example.com/api/content/video',
  data: {
    type: 'poetry',
    id: 1
  },
  success(res) {
    // 处理成功响应
  },
  fail(err) {
    // 处理错误
  }
})
```

**响应数据格式**:
```json
{
  "code": 0,
  "message": "success",
  "data": {
    "id": 1,
    "title": "次北固山下",
    "author": "王湾",
    "dynasty": "唐代",
    "content": "客路青山外，行舟绿水前。潮平两岸阔，风正一帆悬。 海日生残夜，江春入旧年。乡书何处达？归雁洛阳边。",
    "translation": "远方的客路在青山的那边，行船在绿水的前面。涨潮时两岸空阔无边，顺风时船帆高悬。旭日从海上升起，冬去春来又一年。家乡的书信不知寄向何处？只能托付给飞往洛阳的大雁。",
    "videoUrl": "https://example.com/videos/poetry/1.mp4",
    "coverImage": "https://example.com/images/poetry/ci_back1.png"
  }
}
```

### 2. 获取内容详情

**接口描述**: 请求指定分类和ID的内容详细信息

**请求方法**: `GET`

**接口URL**: `/api/content/detail`

**请求参数**:

| 参数名 | 类型   | 是否必须 | 描述                                 |
| ------ | ------ | -------- | ------------------------------------ |
| type   | string | 是       | 内容类型，取值为 `poetry` 或 `prose` |
| id     | number | 是       | 内容ID                               |

**请求示例**:
```javascript
wx.request({
  url: 'https://api.example.com/api/content/detail',
  data: {
    type: 'prose',
    id: 1
  },
  success(res) {
    // 处理成功响应
  },
  fail(err) {
    // 处理错误
  }
})
```

**响应数据格式**:
```json
{
  "code": 0,
  "message": "success",
  "data": {
    "id": 1,
    "title": "小石潭记",
    "author": "柳宗元",
    "dynasty": "唐代",
    "content": "从小丘西行百二十步，隔篁竹，闻水声，如鸣佩环，心乐之。伐竹取道，下见小潭，水尤清冽...(省略)",
    "translation": "从小山丘向西走一百二十步，穿过竹林，听到水声，像佩戴的玉环发出的叮当声，心里感到很愉快...(省略)",
    "annotation": [
      {
        "original": "篁竹",
        "explanation": "指竹林"
      },
      {
        "original": "鸣佩环",
        "explanation": "形容水声清脆悦耳，如同玉佩相互撞击的声音"
      }
    ],
    "appreciation": "《小石潭记》是唐代文学家柳宗元的一篇山水游记，描写了作者被贬永州时游览小石潭的所见所感...(省略)",
    "coverImage": "https://example.com/images/prose/xiao_back1.png"
  }
}
```

### 3. 获取所有内容列表

**接口描述**: 获取所有分类的内容列表

**请求方法**: `GET`

**接口URL**: `/api/content/list`

**请求参数**: 无

**请求示例**:
```javascript
wx.request({
  url: 'https://api.example.com/api/content/list',
  success(res) {
    // 处理成功响应
  },
  fail(err) {
    // 处理错误
  }
})
```

**响应数据格式**:
```json
{
  "code": 0,
  "message": "success",
  "data": {
    "poetry": [
      {
        "id": 1,
        "title": "次北固山下",
        "author": "王湾",
        "dynasty": "唐代",
        "coverImage": "https://example.com/images/poetry/ci_back1.png"
      },
      {
        "id": 2,
        "title": "使至塞上",
        "author": "王维",
        "dynasty": "唐代",
        "coverImage": "https://example.com/images/poetry/shi_back1.png"
      },
      {
        "id": 3,
        "title": "望岳",
        "author": "杜甫",
        "dynasty": "唐代",
        "coverImage": "https://example.com/images/poetry/wang_back1.png"
      }
    ],
    "prose": [
      {
        "id": 1,
        "title": "小石潭记",
        "author": "柳宗元",
        "dynasty": "唐代",
        "coverImage": "https://example.com/images/prose/xiao_back1.png"
      }
    ]
  }
}
```

## 错误码说明

| 错误码 | 描述                   |
| ------ | ---------------------- |
| 0      | 成功                   |
| 1001   | 请求参数错误           |
| 1002   | 内容不存在             |
| 2001   | 服务器内部错误         |
| 3001   | 用户未授权             |
| 3002   | 会话已过期，需要重新登录 |

## 实现示例

以下是一个在小程序中请求内容视频的实现示例：

```javascript
// 请求内容视频
requestContent(e) {
  const { type, id } = e.currentTarget.dataset;
  
  wx.showLoading({
    title: '正在加载',
  });
  
  wx.request({
    url: 'https://api.example.com/api/content/video',
    data: {
      type: type,
      id: id
    },
    header: {
      'content-type': 'application/json'
    },
    success: (res) => {
      wx.hideLoading();
      
      if (res.data.code === 0) {
        const videoUrl = res.data.data.videoUrl;
        // 跳转到视频播放页面
        wx.navigateTo({
          url: `../player/player?videoUrl=${encodeURIComponent(videoUrl)}&title=${encodeURIComponent(res.data.data.title)}`
        });
      } else {
        wx.showToast({
          title: res.data.message || '请求失败',
          icon: 'none'
        });
      }
    },
    fail: () => {
      wx.hideLoading();
      wx.showToast({
        title: '网络请求失败',
        icon: 'none'
      });
    }
  });
}
``` 