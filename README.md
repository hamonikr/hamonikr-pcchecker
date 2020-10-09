# HamoniKR PC Checker

![GitHub
License](https://img.shields.io/github/license/2020-Invesum-Internship/hamonikr-pcchecker)
![GitHub repo
size](https://img.shields.io/github/repo-size/2020-Invesum-Internship/hamonikr-pcchecker)
![GitHub
contributors](https://img.shields.io/github/contributors/2020-Invesum-Internship/hamonikr-pcchecker)
![GitHub
stars](https://img.shields.io/github/stars/2020-Invesum-Internship/hamonikr-pcchecker?style=social)
![GitHub
forks](https://img.shields.io/github/forks/2020-Invesum-Internship/hamonikr-pcchecker?style=social)
![GitHub
issues](https://img.shields.io/github/issues/2020-Invesum-Internship/hamonikr-pcchecker?style=social)

 이 프로그램은 리눅스 데스크탑 사용자의 손쉬운 PC 상태 관리를 위해 만들어
 졌습니다.<br/>
 지원 OS : [HamoniKR 3.0](https://hamonikr.org/), [TmaxOS OE](https://tmaxanc.com/#!/download/TmaxOSOE/product), [Gooroom](https://github.com/gooroom), [Hancom Gooroom](https://github.com/hancomgooroom), [Ubuntu](https://ubuntu.com/), [LinuxMint](https://linuxmint.com/) 에서 사용가능 합니다.


### TODO
 - 바이러스 검사 확인(마지막 검사 후 30일 이내 안전/90일 이내 주의/90일 이상
   위험)
 - 업데이트 상세 확인(보안 업데이트인 경우 기간에 상관없이 위험으로 표시되도록
   변경)
 - 설정 변경시 자동 갱신
 - 디자인 업데이트

<hr>

## 설치 전 요구사항

이 프로그램은 아래의 패키지를 사용하고 있으며 자신이 컴퓨터에 해당 패키지가 없으면 정상 작동되지 않습니다. (하모니카 3.0 은 기본 상태에서 구동.)

* `python 3.6`
* `gtk 3.0`
* `gir1.2-appindicator3-0.1`
* `timeshift`
* `gufw`

## 패키지 설치

터미널(명령 프롬프트)에서 다음과 같이 프로그램 메뉴에 PC 지킴이가 설치할 수 있습니다


## HamoniKR PC Checker 설치

```
sudo add-apt-repository ppa:yeji980407/ppa
sudo apt-get update
sudo apt-get install hamonikr-pcchecker

```

## HamoniKR PC Checker 삭제

```
sudo apt-get --purge remove hamonikr-pcchecker
```

## Using HamoniKR PC Checker

```
프로그램메뉴 > PC 지킴이 실행
```


## Contributing to HamoniKR PC Checker

이 프로젝트에 기여하는 방법은 다음과 같습니다.

1. 이 저장소를 Fork 하세요.
2. 자신이 작업할 branch 를 생성합니다 : `git checkout -b <branch_name>`.
3. 수정사항을 반영하고 커밋합니다 : `git commit -m '<commit_message>'`
4. 저장소에 작업한 브랜치를 Push : `git push origin hamonikr-pcchecker/<location>`
5. pull request 를 생성합니다.

보다 자세한 내용은 GitHub documentation on [creating a pull
request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request) 를 참고하세요.

## Contributors

이 프로젝트에 기여하신 기여자들:

* [@chaeya](https://github.com/chaeya) 📖
* [@Lukehan](https://github.com/LukeHan1128) 🐛

You might want to consider using something like the [All
Contributors](https://github.com/all-contributors/all-contributors)
specification and its [emoji
key](https://allcontributors.org/docs/en/emoji-key).

## Contact

연락이 필요한 경우 <ryuish541@gmail.com> 또는 <yejisoft@gmail.com> 로 내용을 보내주세요.

## License

이 프로젝트는 [GPL3](./LICENSE) 을 따릅니다.


