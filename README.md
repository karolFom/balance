# Описание API
1. POST http://127.0.0.1:1300/api/substract/ - АПИ для уменьшения баланса на счете абонента

Ожидается следующее тело запроса:

`{
	"money": 200,
	"uuid": "jsgdv87kjg-gj"
}
`

money - кол-во денег, на которое нужно уменьшить баланс

uuid  - идентификатор абонента

2. POST http://127.0.0.1:1300/api/add/ - АПИ для увеличения баланса счета абонента

`{
	"money": 200,
	"uuid": "jsgdv87kjg-gj"
}
`

money - кол-во денег, на которое нужно увеличить баланс

uuid  - идентификатор абонента

3. 
# Как развернуть проект

1. Запустить скрипт ./start.sh
2. Выполнить следующую команду для применения миграций:

`docker-compose exec web python manage.py migrate`