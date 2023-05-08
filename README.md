# FCU 選課系統 & 檢索系統
> IECS322 資料庫系統 (許懷中) 期中專題

## Main Window

## Feature

### 主畫面
![](./img/main_windows.png)

### 登入畫面
![](./img/login.png)

### 註冊畫面
![](./img/register.png)

### 檢索結果
![](./img/resault.png.png)

## ER Model
![](./img/er_model.png)

## 設定環境

### Vscode Python 虛擬環境

#### 建立虛擬環境
```
python -m venv venv
```

#### 啟動虛擬環境
```
.\venv\Scripts\Activate.ps1
```

#### 安裝套件
```
pip install -r .\env\requirements.txt
```

#### 關閉虛擬環境
```
deactivate
```

### Python 套件清單

#### pip 生成 requirements.txt

```
pip freeze > .\env\requirements.txt
```

#### pip 使用 requirements.txt

```
pip install -r .\env\requirements.txt
```

### 初始化資料庫

#### 使用 python 匯入
```
python .\database\Databaseinit.py
```

#### phpmyadmin 手動匯入

`.\database\sql\*.sql`

## 組員

邱柏宇 [Poyu39](https://github.com/poyu39)

吳念澤 [kokorosawa](https://github.com/kokorosawa)

徐葆驊 [benhsu0828](https://github.com/benhsu0828)

劉旭峰 [brian1130](https://github.com/brian1130)

葉展綸 [lavacookies](https://github.com/lavacookies)

