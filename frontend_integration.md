# 古典文学小程序前端对接文档

## 项目概述

本文档旨在指导前端开发人员如何与古典文学小程序后端API进行对接。后端基于Python Django框架开发，提供了一系列API接口用于获取古诗和古文的内容、视频等资源。

## 基础信息

- **基础URL**: `https://your-domain.com`（请替换为实际部署的域名）
- **API版本**: v1
- **数据格式**: JSON
- **编码**: UTF-8
- **认证方式**: 无需认证

## API接口

### 1. 获取内容列表

获取所有古诗和古文的列表信息。

**请求方式**: `GET`

**接口路径**: `/api/content/list`

**请求参数**: 无

**响应示例**:
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
        "cover_image": "/images/poetry/ci_back1.png"
      },
      {
        "id": 2,
        "title": "使至塞上",
        "author": "王维",
        "dynasty": "唐代",
        "cover_image": "/images/poetry/shi_back1.png"
      }
    ],
    "prose": [
      {
        "id": 1,
        "title": "小石潭记",
        "author": "柳宗元",
        "dynasty": "唐代",
        "cover_image": "/images/prose/xiao_back1.png"
      }
    ]
  }
}
```

**小程序实现示例**:
```javascript
// pages/index/index.js
Page({
  data: {
    poetryList: [],
    proseList: []
  },
  
  onLoad: function() {
    this.getContentList();
  },
  
  getContentList: function() {
    wx.showLoading({
      title: '加载中',
    });
    
    wx.request({
      url: 'https://your-domain.com/api/content/list',
      method: 'GET',
      success: (res) => {
        if (res.data.code === 0) {
          this.setData({
            poetryList: res.data.data.poetry,
            proseList: res.data.data.prose
          });
        } else {
          wx.showToast({
            title: res.data.message || '获取内容列表失败',
            icon: 'none'
          });
        }
      },
      fail: () => {
        wx.showToast({
          title: '网络请求失败',
          icon: 'none'
        });
      },
      complete: () => {
        wx.hideLoading();
      }
    });
  }
});
```

### 2. 获取内容视频

获取指定类型和ID的内容的视频地址和基本信息。

**请求方式**: `GET`

**接口路径**: `/api/content/video`

**请求参数**:

| 参数名 | 类型   | 是否必须 | 描述                                 |
| ------ | ------ | -------- | ------------------------------------ |
| type   | string | 是       | 内容类型，取值为 `poetry` 或 `prose` |
| id     | number | 是       | 内容ID                               |

**响应示例**:
```json
{
  "code": 0,
  "message": "success",
  "data": {
    "id": 1,
    "title": "次北固山下",
    "author": "王湾",
    "dynasty": "唐代",
    "content": "客路青山外，行舟绿水前。潮平两岸阔，风正一帆悬。\n海日生残夜，江春入旧年。乡书何处达？归雁洛阳边。",
    "translation": "远方的客路在青山的那边，行船在绿水的前面。涨潮时两岸空阔无边，顺风时船帆高悬。旭日从海上升起，冬去春来又一年。家乡的书信不知寄向何处？只能托付给飞往洛阳的大雁。",
    "video_url": "/videos/poetry/ci_bei_gu.mp4",
    "cover_image": "/images/poetry/ci_back1.png"
  }
}
```

**小程序实现示例**:
```javascript
// pages/detail/detail.js
Page({
  data: {
    content: null,
    videoContext: null
  },
  
  onLoad: function(options) {
    const { type, id } = options;
    this.getContentVideo(type, id);
  },
  
  onReady: function() {
    this.videoContext = wx.createVideoContext('contentVideo');
  },
  
  getContentVideo: function(type, id) {
    wx.showLoading({
      title: '加载中',
    });
    
    wx.request({
      url: 'https://your-domain.com/api/content/video',
      method: 'GET',
      data: {
        type: type,
        id: id
      },
      success: (res) => {
        if (res.data.code === 0) {
          // 将完整域名添加到视频URL和封面图片URL
          const data = res.data.data;
          data.video_url = 'https://your-domain.com' + data.video_url;
          data.cover_image = 'https://your-domain.com' + data.cover_image;
          
          this.setData({
            content: data
          });
        } else {
          wx.showToast({
            title: res.data.message || '获取内容视频失败',
            icon: 'none'
          });
        }
      },
      fail: () => {
        wx.showToast({
          title: '网络请求失败',
          icon: 'none'
        });
      },
      complete: () => {
        wx.hideLoading();
      }
    });
  }
});
```

**WXML示例**:
```html
<!-- pages/detail/detail.wxml -->
<view class="container" wx:if="{{content}}">
  <view class="header">
    <text class="title">{{content.title}}</text>
    <view class="meta">
      <text class="author">{{content.author}}</text>
      <text class="dynasty">{{content.dynasty}}</text>
    </view>
  </view>
  
  <video id="contentVideo" 
         src="{{content.video_url}}" 
         poster="{{content.cover_image}}" 
         controls>
  </video>
  
  <view class="content-section">
    <view class="section-title">原文</view>
    <text class="content-text">{{content.content}}</text>
  </view>
  
  <view class="content-section">
    <view class="section-title">翻译</view>
    <text class="content-text">{{content.translation}}</text>
  </view>
</view>
```

### 3. 获取内容详情

获取指定类型和ID的内容的详细信息，包括注释、赏析等。

**请求方式**: `GET`

**接口路径**: `/api/content/detail`

**请求参数**:

| 参数名 | 类型   | 是否必须 | 描述                                 |
| ------ | ------ | -------- | ------------------------------------ |
| type   | string | 是       | 内容类型，取值为 `poetry` 或 `prose` |
| id     | number | 是       | 内容ID                               |

**响应示例**:
```json
{
  "code": 0,
  "message": "success",
  "data": {
    "id": 1,
    "title": "小石潭记",
    "author": "柳宗元",
    "dynasty": "唐代",
    "content": "从小丘西行百二十步，隔篁竹，闻水声，如鸣佩环，心乐之。伐竹取道，下见小潭，水尤清冽...",
    "translation": "从小山丘向西走一百二十步，穿过竹林，听到水声，像佩戴的玉环发出的叮当声，心里感到很愉快...",
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
    "appreciation": "《小石潭记》是唐代文学家柳宗元的一篇山水游记，描写了作者被贬永州时游览小石潭的所见所感...",
    "cover_image": "/images/prose/xiao_back1.png",
    "video_url": "/videos/prose/xiao_shi_tan.mp4"
  }
}
```

**小程序实现示例**:
```javascript
// pages/detailed/detailed.js
Page({
  data: {
    content: null
  },
  
  onLoad: function(options) {
    const { type, id } = options;
    this.getContentDetail(type, id);
  },
  
  getContentDetail: function(type, id) {
    wx.showLoading({
      title: '加载中',
    });
    
    wx.request({
      url: 'https://your-domain.com/api/content/detail',
      method: 'GET',
      data: {
        type: type,
        id: id
      },
      success: (res) => {
        if (res.data.code === 0) {
          // 将完整域名添加到封面图片URL
          const data = res.data.data;
          data.cover_image = 'https://your-domain.com' + data.cover_image;
          
          this.setData({
            content: data
          });
        } else {
          wx.showToast({
            title: res.data.message || '获取内容详情失败',
            icon: 'none'
          });
        }
      },
      fail: () => {
        wx.showToast({
          title: '网络请求失败',
          icon: 'none'
        });
      },
      complete: () => {
        wx.hideLoading();
      }
    });
  }
});
```

**WXML示例（古文详情页）**:
```html
<!-- pages/detailed/detailed.wxml -->
<view class="container" wx:if="{{content}}">
  <image class="cover-image" src="{{content.cover_image}}" mode="aspectFill"></image>
  
  <view class="header">
    <text class="title">{{content.title}}</text>
    <view class="meta">
      <text class="author">{{content.author}}</text>
      <text class="dynasty">{{content.dynasty}}</text>
    </view>
  </view>
  
  <view class="tabs">
    <view class="tab-item active">内容</view>
    <view class="tab-item">注释</view>
    <view class="tab-item">赏析</view>
  </view>
  
  <swiper class="content-swiper" current="{{currentTab}}">
    <swiper-item>
      <view class="content-section">
        <view class="section-title">原文</view>
        <text class="content-text">{{content.content}}</text>
      </view>
      <view class="content-section">
        <view class="section-title">翻译</view>
        <text class="content-text">{{content.translation}}</text>
      </view>
    </swiper-item>
    
    <swiper-item>
      <view class="annotation-list">
        <view class="annotation-item" wx:for="{{content.annotation}}" wx:key="index">
          <text class="annotation-original">{{item.original}}</text>
          <text class="annotation-explanation">{{item.explanation}}</text>
        </view>
      </view>
    </swiper-item>
    
    <swiper-item>
      <view class="appreciation-content">
        <text>{{content.appreciation}}</text>
      </view>
    </swiper-item>
  </swiper>
  
  <view class="action-button" bindtap="watchVideo">
    观看视频讲解
  </view>
</view>
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

## 最佳实践

1. **错误处理**：始终检查响应中的`code`字段，只有当`code`为0时才处理数据，否则显示错误信息。

2. **加载状态**：在发起请求前显示加载提示，请求完成后隐藏。

3. **资源路径**：注意视频和图片URL是相对路径，需要拼接服务器域名。

4. **缓存策略**：可以考虑缓存内容列表和常用内容，减少网络请求。

5. **网络异常**：处理网络请求失败的情况，提供友好的用户提示。

6. **UI适配**：确保在不同尺寸的设备上都有良好的显示效果。

## 前端页面规划

1. **首页**：展示古诗和古文的分类列表
   - 调用`/api/content/list`接口获取所有内容
   - 可以添加轮播图展示推荐内容

2. **视频播放页**：播放内容相关视频并显示基本信息
   - 调用`/api/content/video`接口获取视频和基本信息
   - 使用小程序的video组件播放视频

3. **详情页**：展示内容的详细信息，包括原文、翻译、注释和赏析
   - 调用`/api/content/detail`接口获取详细信息
   - 使用选项卡切换不同内容

## 联系方式

如在对接过程中遇到问题，请联系后端开发负责人：

- 邮箱：[backend@example.com](mailto:backend@example.com)
- 电话：123-4567-8910 