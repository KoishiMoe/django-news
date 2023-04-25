基于django的简单新闻网站/博客
==============================
Web开发课程作业，突出一个能用就行

## 功能
- [x] 用户注册/登录/登出
- [ ] 用户修改密码（目前只能通过管理员修改）
- [x] 创建、修改、删除文章
- [x] 创建、修改、删除评论（修改和删除只能管理员操作）
- [x] 分类和子分类
- [x] 后台管理

## 已知问题

* charts不能用，不是我写的，我也懒得修，就酱
* 已有子分类的分类仍然可以被设置为子分类

## 依赖
建议用poetry安装依赖
```bash
poetry install
```

当然你也可以用pip
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 运行
首次运行需要初始化数据库和静态文件
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
```

然后就可以运行了
```bash
python manage.py runserver
```

## issue和pull request
玩具项目，不接受issue。如果你想改进这个项目，可以fork到你自己的仓库，然后随便改，不用提pr。

## 许可证
AGPLv3，`apps/charts`目录以及`templates/stock_*.html`除外，因为不是我写的
