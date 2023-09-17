# saleAuto 


## BUILT-IN
- Python;
- FastAPI + SQLAlchemy + Pydantic + Alembic;
- PostgreSQL;
- RabbitMQ (temporarily __canceled__);
- k8s (temporarily __canceled__);
- Redis;
- aiogram;
- VueJS (NuxtJS);
- docker, docker-compose;
- nginx;
- [SQLAlchemyAdmin](https://github.com/aminalaee/sqladmin);
- to be continued...


## CONCEPT

### summary
> Веб-сервис, обеспечивающий предложение и администрирование услуг и торговых операций в автомобильной отрасли для проекта **saleAuto**.
> 
### roadmap
- [ ] Gateway, обрабатывающий запросы к серверу и подзапросы к сервисам;
- [ ] Микросервис, обрабатывающий бизнес-процессы (пользователи -> заявки -> звонки -> сделки -> расчеты -> __договоры__ (?);
- [ ] Микросервис, обрабатывающий уведомление (__TG__, __EMail__, __SMS__) пользователей и администраторов, владельцев бизнеса о бизнес-операциях;
- [ ] Микросервис, обрабатывающий парсинг нужных данных для составления/дополнения пользовательских заявок по услугам компании;
- [ ] Telegram-бот, предлагающий администратору (владельцу) контроль над всеми бизнес-процессами (-сущностями) в доступной форме (CRUD).

### business-scheme
> [draw.io common scheme](docs/AppDiagram.drawio)
> 
### business-logic & technical requirements
> [document](docs/business_logics.md)


## CONTRIBUTORS
+ [Dahaka1](https://github.com/Dahaka1) - backend-dev;
+ waiting for another ...