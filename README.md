# 한국생물공학회 교육워크샵
12월 한국생물공학회 교육워크샵의 [생물공학 기계학습] 실습 (튜토리얼 Day1) 사이트 입니다.

# 최종 실습 pdf 자료
- [docker 설치 메뉴얼](https://github.com/greendaygh/bioengml/blob/master/%EC%83%9D%EB%AC%BC%EA%B3%B5%ED%95%99%EA%B8%B0%EA%B3%84%ED%95%99%EC%8A%B5-%EC%9B%8C%ED%81%AC%EC%83%B5%EC%82%AC%EC%A0%84%EC%A4%80%EB%B9%84-20191217%20%EB%A9%94%EB%89%B4%EC%96%BC.pdf)
- [튜토리얼1-소개](https://github.com/greendaygh/bioengml/blob/master/%ED%8A%9C%ED%86%A0%EB%A6%AC%EC%96%BC1-%EC%86%8C%EA%B0%9C-20191219.pdf)
- [튜토리얼1-실습-docker](https://github.com/greendaygh/bioengml/blob/master/%ED%8A%9C%ED%86%A0%EB%A6%AC%EC%96%BC1-%EC%8B%A4%EC%8A%B5-20191219.pdf)
- [튜토리얼1-실습-colab](https://github.com/greendaygh/bioengml/blob/master/%ED%8A%9C%ED%86%A0%EB%A6%AC%EC%96%BC1-%EC%8B%A4%EC%8A%B5-colab-20191219.pdf)

# 최종 실습 jupyter lab 자료
- [튜토리얼1-실습-docker](https://github.com/greendaygh/bioengml/blob/master/%ED%8A%9C%ED%86%A0%EB%A6%AC%EC%96%BC1-%EC%8B%A4%EC%8A%B5-20191219.ipynb)
- [튜토리얼1-실습-colab](https://github.com/greendaygh/bioengml/blob/master/%ED%8A%9C%ED%86%A0%EB%A6%AC%EC%96%BC1-%EC%8B%A4%EC%8A%B5-colab-20191219.ipynb)

# Docker run for MacOS
docker run --rm -it -d -p 8888:8888  --name bioengml -v /tmp/bioengml:/home/bioengml haseong/bioengml:v1 jupyter lab --no-browser --allow-root --ip=0.0.0.0 --notebook-dir=/home/bioengml --NotebookApp.token=

# git clone from bioengml to google drive in colab env.
!git clone https://github.com/greendaygh/bioengml.git "/content/drive/My Drive/Colab Notebooks/bioengml"
