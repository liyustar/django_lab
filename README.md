# 环境部署

## 激活虚拟 Python 环境
```
conda create --name python37 python=3.7
source activate python37
```

## 依赖导入导出
```
# 导出
conda env export > environment.yaml

# 导入
conda env create -f environment.yaml
```

# 服务启动
```
python manager.py runserver
```

## 数据表构建
```
python manager.py makemigrations
python manager.py migrate
```


