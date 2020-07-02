Esse foi um projeto de site para o nosso casamento criado por mim e minha noiva, formada em Matemática, a quem eu estava ensinando a programar.

# Inicializando

## Criando mutation autogerada e atualizando banco de dados
```sh
flask db revision --autogenerate -m "Short comment"
flask db upgrade head
```

## Rodando servidor
```sh
export FLASK_APP=main.py
export FLASK_ENV=development
flask run --host=0.0.0.0
```

## Autopep8
```sh
autopep8 --in-place --aggressive --aggressive ./app/**/*.py*
```