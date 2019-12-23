# 한국생물공학회 교육워크샵
12월 한국생물공학회 교육워크샵의 [생물공학 기계학습] 실습 (튜토리얼 Day1) 사이트 입니다.

# 최종 실습 pdf 자료
## 강의 자료
- [docker 설치 메뉴얼](https://github.com/greendaygh/bioengml/blob/master/%EC%83%9D%EB%AC%BC%EA%B3%B5%ED%95%99%EA%B8%B0%EA%B3%84%ED%95%99%EC%8A%B5-%EC%9B%8C%ED%81%AC%EC%83%B5%EC%82%AC%EC%A0%84%EC%A4%80%EB%B9%84-20191217%20%EB%A9%94%EB%89%B4%EC%96%BC.pdf)
- [튜토리얼1-소개]() 
- [튜토리얼1-실습-docker]()
- [튜토리얼1-실습-colab]()

# Docker run for MacOS
docker run --rm -it -d -p 8888:8888  --name bioengml -v /tmp/bioengml:/home/bioengml haseong/bioengml:v1 jupyter lab --no-browser --allow-root --ip=0.0.0.0 --notebook-dir=/home/bioengml --NotebookApp.token=

# git clone from bioengml
!git clone https://github.com/greendaygh/bioengml.git "/content/drive/My Drive/Colab Notebooks/bioengml"
