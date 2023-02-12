# Characterization-of-ligands-that-bind-to-human-delta-mu-opioid-receptor-heterodimers
### 1. 目的
ヒトδ-μオピオイド受容体ヘテロダイマーに結合するリガンドの特徴解析

### 2. 使い方
本研究では、PCA, t-SNE, UMAPという3つのフォルダそれぞれで作業をしている。 まず、それぞれのフォルダにno3d_add_id.csvというファイルを入れる。これは、masterというブランチに入れてある。 以下方法の手順に沿って説明する。詳しい方法は卒業論文を参照してください。

3-1. 各リガンドをStructure Data File(SDF)に変換して構造情報を取得 uniD.csv, uniM.csv, M_DM_D_ID.csvの3つのファイルを用いて、SDFを算出した。

3-2. Mordredを用いた分子記述子の作成 Mordred.pyというスクリプトを用いて算出している。3-1で作成したSDFを用いている。

3-3. 次元削減アルゴリズムによる散布図の作成 hetero_PCA.py, hetero_t-SNE.py, hetero_umap.pyというスクリプトを用いて散布図を作成した。 散布図のX軸Y軸の座標をcsvファイルに保存した。

3-4. 散布図のヒートマップ化 3-3で作成したcsvファイルを用いてヒートマップを作成した。heatmap.pyというスクリプトを用いた。

### 3．環境
- Python 3.10.5

### 4．文責
瀧島 僚太

###　5．ライセンス
