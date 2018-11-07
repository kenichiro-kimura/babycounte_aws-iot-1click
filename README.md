# AWS IoT 1-click Button��Ȥä��֤����γ�ư��Ͽ

## ����

�֤���󤬾������Ȥ��ϡ�����������ε�Ͽ��Ĥ���ΤϤȤƤ����ڤǤ���
���������ºݤˤ���Ȥ��Ƥ⾮�����֤��������򤷤ʤ���ޥ�˥Ρ��Ȥ˽񤯤ΤϤȤƤ����ѤǤ���
�����ǡ�����ƥܥ���1����å��ǥ��٥�ȤȤ��λ��֤����Ǥ⵭Ͽ�Ǥ���ФȤλפ�����������ޤ���

## �Ȥ�������

AWS�Υ�������Ȥκ�����ʤɤξܺ٤�Ŭ��Ĵ�٤Ƥ�������

- python2.7�򥤥󥹥ȡ��뤹��
- AWS�Υ�������Ȥ��ꡢaws cli��ư���褦�ˤ���
- ������(https://aws.amazon.com/jp/iot-1-click/devices/)�򸫤ƥǥХ��������ꤹ��
  - �Ŀ�Ū�ˤ���³����ñ�����Ӥ��Ѥ�����SORACOM LTE-M Button powered by AWS(https://pages.soracom.jp/LP_SORACOM-LTE-M-Button.html)��������Ǥ���
- git clone����
- serverless framework�򥤥󥹥ȡ��뤹��
  ```bash
  %pip install serverless
  ```
- ɬ�פʥ饤�֥��������
  ```bash
  %pip install -r requirements.txt -t ./
  ```
- ��ꤢ�����ǥץ�����
  ```bash
  %sls deploy
  ```
- LINE Messaging API��Developer Trial(̵��)����󤷤ƥܥåȥ�������Ȥ���
- �ǥץ�����ɽ�����줿API Gateway��URL��Messaging API�Υ�����Хå�����Ͽ����
- �ܥåȥ�������Ȥ�LINE��ͧã�ˤʤꡢŬ���ʥ��롼�פ�������Ƥ����˾��Ԥ���
- AWS�Υ��󥽡��뤫�顢Lambda�ؿ���babyconter-hello-dev�פ�CloudWatch Logs�򸫤�ȥ��롼�׾��ԤΥ��٥�ȥ����ФƤ�Ϥ��ʤΤǡ�groupId�פ���ʬ���������config.ini�˵��ܤ���
- google��credential���������
  - https://console.developers.google.com/project �˥�������
  - [�ץ������Ⱥ���] �ˤƥץ������Ȥ����
  - ���������ץ������Ȥ� API Manager ���� [Drive API] �򥯥�å�
  - Google Drive API �ˤ� [ͭ���ˤ���] �򥯥�å�
  - API Manager �Υ�˥塼���� [ǧ�ھ���] �򥯥�å�
  - [�����ӥ� ���������] �ץ�������� [�����������ӥ����������] �򥯥�å�
  - [�����ӥ� ���������̾] ��Ǥ�դ�̾��������
  - [���] �ˤ� [Project] �� [�Խ���] �򥯥�å�
  - [�����Υ�����] �� [JSON] ������
  - �Ǹ�� [����] �ܥ���򥯥�å�
  ����Ǽ��������ե������Ŭ����̾����git clone�����ǥ��쥯�ȥ���֤����ե�����̾��config.ini�˵��ܤ���
- google���ץ�åɥ����Ȥο����ե��������������嵭��credential�˴ޤޤ��᡼�륢�ɥ쥹���Ф��ƶ�ͭ��Ф�
- google���ץ�åɥ����ȤΥ�����̾�ȡ�ID(URL��https://docs.google.com/spreadsheets/d/hogehoge/...�ȤʤäƤ���Ȼפ��Τǡ����Ρ�hogehoge�פ���ʬ)���������config.ini�˽�
- �⤦1��ǥץ�����
  ```bash
  %sls deploy
  ```
- �ܥ����Ҥ�Ť���
  - AWS�Υ��󥽡���ʤ�����CLI�ǡ��������줿Lambda�ؿ���babyconter-sendmsg-dev�פ˥ܥ����Ҥ�Ť���


 
