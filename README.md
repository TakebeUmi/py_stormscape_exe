説明：
「A minimal Stable Fluids inspired fluid solver with Python and NumPy.」をもとに「Stormscapes: simulating cloud dynamics in the now」の論文の内容をコードとして再現し、openvdbとして出力するコードになります。
具体的な使い方を以下に示します。ディレクトリ内で「python main.py」実行すると、いくつかのパラメータの値の入力を求められます。各パラメータは以下のような特徴を持ち、値によって計算結果が変化します。

φrel：地表面における湿度。０～１の値を持ち、大きいほど地表面に近い部分で雲ができやすくなる
γheat：地表面の熱量を示すパラメータ。０～２程度の値を持ち、大きいほど地表面の温度が高くなる
γvapor：地表面の水蒸気分布を示すパラメータ。０～１の値を持ち、大きいほど地表面から排出される水蒸気量が多くなり、系全体の雲の量が多くなりやすくなる。

これを打ち込んだのち「calculation start!」のボタンを押すことで計算が実行され、結果となるvdbファイルがoutputに出力されます。通常は計算をして初めて結果が得られますが、事前に計算された結果がすでに格納されています。

Citations:\
[Stormscapes: simulating cloud dynamics in the now](https://dl.acm.org/doi/10.1145/3414685.3417801)
[Philip Zucker's blog post on fluid simulation](http://www.philipzucker.com/annihilating-my-friend-will-with-a-python-fluid-simulation-like-the-cur-he-is/)\
[GPUGems fast fluid simulation guide](http://developer.download.nvidia.com/books/HTML/gpugems/gpugems_ch38.html)\
[Jos Stam's legendary paper](https://d2f99xq7vri1nk.cloudfront.net/legacy_app_files/pdf/ns.pdf)\
[Cameron Taylor's finite difference coefficient calculator and derivation](http://web.media.mit.edu/~crtaylor/calculator.html)
[A minimal Stable Fluids inspired fluid solver with Python and NumPy.](https://github.com/GregTJ/stable-fluids)
