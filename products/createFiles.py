for i in range(19):
	myFile = open(f'{i+1}.html', 'w+', encoding='UTF-8')
	myFile.write(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../css/style.css">
    <link rel="stylesheet" href="../css/product.css">
    <title></title>
</head>
<body data-product-id='{i+1}'>
    <header>
        <div class="wrapper">
            <nav>
                <div class="left-btns">
                    <div class="btn home"><a href="../index.html"><img src="../img/home.png" alt=""></a></div>
                    <div class="btn"><a href="../catalog.html"><img src="../img/list.png" alt="" class="btn-img">Каталог</a></div>
                </div>
                <div class="search">
                    <img src="../img/search.png" alt="">
                    <input type="text">
                </div>
                <div class="right-btns">
                    <div class="btn"><a href="../reviews.html"><img src="../img/feedback.png" alt="" class="btn-img">Отзывы</a></div>
                    <div class="btn cart-btn"><a href="../cart.html"></img src="../img/shopping-cart.png" alt="" class="btn-img"> Корзина</a></div>
                </div>
            </nav>
        </div>
    </header>
    <div class="product-wrapper">
        <div class="wrapper">
            <div class="title"></div>
            <div class="product">
                
            </div>
            <div class="title teh">Технические характеристики</div>
            <table>
                <tr>
                    <td>Площадь уборки на одном заряде, м2</td>
                    <td>До 60</td>
                </tr>
                <tr>
                    <td>Комплект поставки</td>
                    <td>Напольная зарядная база/Аккумуляторная батарея</td>
                </tr>
                <tr>
                    <td>Количество убираемых комнат</td>
                    <td>до 2-х</td>
                </tr>
                <tr>
                    <td>Время работы на одном заряде, часов</td>
                    <td>1.5 ч</td>
                </tr>
                <tr>
                    <td>Заряжается самостоятельно</td>
                    <td>Да</td>
                </tr>
                <tr>
                    <td>Локальная уборка</td>
                    <td>Нет</td>
                </tr>
                <tr>
                    <td>Возобновление уборки после подзарядки</td>
                    <td>Нет</td>
                </tr>
                <tr>
                    <td>Программирование графика уборки</td>
                    <td>Да</td>
                </tr>
                <tr>
                    <td>Управление со смартфона</td>
                    <td>Да</td>
                </tr>
                <tr>
                    <td>Улучшенная система уборки – AeroForce</td>
                    <td>Нет</td>
                </tr>
            </table>
        </div>
    </div>
    <footer>
        <div class="wrapper footer-blocks">
            <div class="shop-name">
                Интернет магазин RCleaner
            </div>
            <div class="btn-links">
                <a href="../catalog.html">Каталог товаров</a>
                <a href="../cart.html">Корзина</a>
                <a href="../news.html">Новости</a>
            </div>
            <div class="shop-contants">
                <div><b>Наши данные:</b></div>
                <div class="nubmer">Наш номер телефона: <b>+7999999999</b></div>
                <div class="mail">Наша почта: <b>shop@rcleaner.ru</b></div>
            </div>
        </div>
    </footer>
    <script src="../info.js"></script>
    <script src="../buy.js"></script>
    <script src="../cartProductsAmount.js"></script>
</body>
</html>
		""")
	myFile.close();
	print('OK');