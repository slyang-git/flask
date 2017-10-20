
                          // Flask //

       because a pocket knife is not the only thing that
                      might come in handy


    ~ What is Flask?

      Flask is a microframework for Python based on Werkzeug
      and Jinja2.  It's intended for small scale applications
      and was development with best intentions in mind.

    ~ Is it ready?

      Nope, this is still work in progress, but I am happy to
      accept patches and improvements already.

    ~ What do I need?

      Jinja 2.4 and Werkzeug 0.6.1.  `easy_install` will
      install them for you if you do `easy_install Flask==dev`.
      I encourage you to use a virtualenv.  Check the docs for
      complete installation and usage instructions.

    ~ Where are the docs?

      Go to http://flask.pocoo.org/ for a prebuild version of
      the current documentation.  Otherwise build them yourself
      from the sphinx sources in the docs folder.

### 阅读笔记—— release 0.1

#### 一、前言

阅读开源项目源代码也是有套路的，有人会直接从Github上 fork或者clone一个开源项目，然后就开始阅读。这是不科学的。

一个项目不是一口气写完的，而是作者经过很多次迭代打磨，甚至还有很多其他开源贡献者共同的一次次commit成就的。而最佳的入门方式，应该是从项目的最早的一个release版本开始着手阅读。

因为：
1. 代码量最少，文件量最少，便于立即着手阅读，而不是花费半天时间去立即每一个模块，文件的依赖关系；
2. 此时的代码是核心代码。项目迭代过程会加上很多容错、兼容、健壮性代码，但是这些代码并不是项目的核心代码，而是优化代码。
3. 便于立即跑通代码。

基于以上三个原因。我们开启Flask的源码阅读之路。

#### 二、环境准备

Flask的最早release版本是 0.1，Python解释器是2.X版本，所以最好是用virtualenv来新建一个虚拟环境。另外，Flask还依赖Werkzeug和Jinja2两个包，
并且这两个包发展到目前也已经迭代了很多版本，如果是0.1版本的Flask，应该是需要恢复到当时的Werkzeug和Jinja2版本。所以，环境准备的目的是为了尽量恢复到
0.1版本开发时候的环境，排除其他干扰。

首先 checkout 0.1 版本

git checkout 0.1

为了不破坏"犯罪现场"，我们立即从0.1版本再次checkout一个新的版本，我把它命名为 `source_code_reading_0.1`

到此时，依赖的Werkzeug和Jinja2两个包还没有安装好，可以在项目的根目录下看到有一个名为 setup.py的文件，里面有依赖的Werkzeug和Jinja2两个包的版本号（注意里面的依赖是 >=, 需要改成 == 号，才会安装对应的低版本号，如果不这样做，）。
运行命令 python setup.py install

现在，已经到了一个全新的 0.1版本分支了，在这个分支上，我们可以随意更改代码，调试代码，最好commit代码。
