# 한국생물공학회 교육워크샵
12월 한국생물공학회 교육워크샵의 [생물공학 기계학습] 실습 (튜토리얼 Day1) 사이트 입니다.

# 최종 실습 pdf 자료

#

# Docker run for MacOS
docker run --rm -it -d -p 8888:8888  --name bioengml -v /tmp/bioengml:/home/bioengml haseong/bioengml:v1 jupyter lab --no-browser --allow-root --ip=0.0.0.0 --notebook-dir=/home/bioengml --NotebookApp.token=

# git clone from bioengml
!git clone https://github.com/greendaygh/bioengml.git "/content/drive/My Drive/Colab Notebooks/bioengml"
