
function getTemperatureFromElement() {
    var tempText = $('#external-temperature').text();
    
    var tempValue = tempText.replace(/[^\d.-]/g, '');
    
    var tempNumber = parseFloat(tempValue);
    
    // console.log(tempNumber);
    return tempNumber;
}
function delta_math(t1, t2) {
    if (t1 < t2) {
        return t2 - t1
    } else {
            return t1 - t2
        }
    }
    
    function calc_temp_into(lambda, width, t1, t2) {
        return lambda/width * delta_math(t1, t2);
    }
    
    function plotTemperatureCurve(t1, t2, delta) {
        // Генерация значений x от 0 до толщины стенки
        var xValues = [];
        var yValues = [];
        for (var x = 0; x <= delta; x += delta / 100) {
            xValues.push(x);
            var tx = t1 - (delta_math(t1, t2)) / delta * x;
            yValues.push(tx);
        }
        var trace = {
            x: xValues,
            y: yValues,
            type: 'scatter',
            mode: 'lines+markers',
            marker: { size: 4 }
        };
        
        var data = [trace];
        
        var layout = {
            title: 'Температурная кривая в стенке',
            xaxis: {
                title: 'Расстояние (м)'
            },
            yaxis: {
                title: 'Температура (°C)'
            }
        };

        Plotly.newPlot('temperature-graph', data, layout);
    }
    

function calculateThermalResistance(d, k) {
    // Рассчитывает тепловое сопротивление стены
    // d: Толщина стены (в метрах).
    // k: Коэффициент теплопроводности материала стены (в Вт/(м·°C)).
    return d / k;
}
function calc_square(a, b, z) {
    return a * z * 2 + a * b * 2 + b * z * 2;
}

function calc_cube(a, b, z) {
    return a * z * b;
}

function calc_mass(v) {
    return 1,29 * v;
}


function calculateHeatLoss(deltaT, A, t, R) {
    // Рассчитывает количество тепла, переданного через стену или стенки.
    // deltaT: Разность температур снаружи и внутри (в градусах Цельсия).
    // A: Площадь стены или общая площадь стенок (в квадратных метрах).
    // t: Время в секундах.
    // R: Тепловое сопротивление стены или стенок (в м²·°C/W).
    return (deltaT * A * t) / R;
}

function calculateTemperatureChange(Q, m, cp) {
    // Рассчитывает изменение температуры в помещении на основе потерь тепла.
    // Q: Количество тепла, переданного через стену (в Джоулях).
    // m: Масса воздуха в помещении (в кг).
    // cp: Теплоемкость воздуха (в Дж/(кг·°C)).
    return Q / (m * cp);
}

function updateResistor(d, k) {
    var temp_into = calculateThermalResistance(d,k);
    $('#temp-resistor').html('Tепловое сопротивление стены: ' + temp_into.toFixed(6) + '<br>Считается по формуле: d/k <br> d: Толщина стены (в метрах). <br>k: Коэффициент теплопроводности материала стены (в Вт/(м·°C)).<br><br>');
    return temp_into
}

function updateHeat(deltaT, A, t, R) {
    var temp_into = calculateHeatLoss(deltaT, A, t, R);
    $('#temp-q').html('Kоличество тепла, переданного через стены (в Джоулях): ' + temp_into.toFixed(6) + '<br>Считается по формуле: (deltaT * A * t) / R <br> deltaT: Разность температур снаружи и внутри (в градусах Цельсия)<br>A: Площадь стены или общая площадь стенок (в квадратных метрах).<br>t: Время в секундах<br>R: Тепловое сопротивление стены или стенок (в м²·°C/W)<br><br>');
    return temp_into
}

function updateTemperatureChange(Q, m, cp) {
    var temp_into = calculateTemperatureChange(Q, m, cp);
    $('#temp-t').html('Изменение температуры в помещении на основе потерь тепла: ' + temp_into.toFixed(6) + '<br>Считается по формуле: Q / (m * cp) <br> Q: Количество тепла, переданного через стену (в Джоулях).<br>m: Масса воздуха в помещении (в кг).<br>cp: Теплоемкость воздуха (в Дж/(кг·°C)).<br><br>');
    return temp_into
}


    function getTemperature() {
        var apiKey = 'e2e6375d2129535d6cc7a57b7c4d23c3';
        var url = `http://api.openweathermap.org/data/2.5/weather?q=Moscow,ru&appid=${apiKey}&units=metric`;
        
        // Возвращаем Promise
        return new Promise((resolve, reject) => {
            $.getJSON(url, function(data) {
                if (data && data.main && data.main.temp) {
                    resolve(data.main.temp);
                } else {
                    reject("Temperature data is not available");
                }
        }).fail(function() {
            reject("Failed to load temperature data");
        });
    });
}

async function updateTemperature() {
    try {
        console.log("ready")
        var temperature = await getTemperature(); // ожидаем получения температуры
        
        $('#external-temperature').text('Внешняя температура в Москве: ' + temperature.toFixed(1) + '°C');
    } catch (error) {
        console.error("An error occurred:", error);
        // Обработка ошибки, если API не вернул температуру
    }
}

        // Функция для расчета
        function calculatePerimeter(name) {
            var width = parseFloat(document.getElementById(`width${name}`).value) / 1000;
            var height = parseFloat(document.getElementById(`height${name}`).value) / 1000;
            // var room_size = parseFloat(document.getElementById(`room_size${name}`).value) / 1000;
            
            // var price_for_meter = parseFloat(document.getElementById('price_in').value)
            
            var formulaDescription = "Периметр = (ширина + длина + высота) * 4\n\n" +
            "Площадь стен = (ширина * высота * 2) + (длина * высота * 2) + (ширина * размер комнаты * 2) \n\n" +
            "Объем комнаты = ширина * высота * длина.\n\n" +
            "Площадь стены a = высота * длина.\n\n" +
            "Площадь стены b = ширина * высота.\n\n" +
            "Площадь пола/потолка = ширина * длина.\n\n" +
            "Итоговая стоимость материала = цена за м^2 * площадь стен.\n\n";
            document.getElementById('formula').innerText = formulaDescription;

            // Проверяем, что все значения введены
            // if (!isNaN(width) && !isNaN(height) && !isNaN(room_size)) {
            if (!isNaN(width) && !isNaN(height)) {
                // var perimeter = (width + room_size+ height) * 4;
                // var room_size = 0
                // var perimeter = (width + height) * 2;
                // var square = (width * height * 2) + room_size * height * 2 + width * room_size * 2
                var square = (width * height)
                // var cube = (width * height * room_size)
                // var square_a = height * room_size
                // var square_b = width * height
                // var square_floor = room_size * width
                // document.getElementById('perimeter').value = perimeter;
                document.getElementById(`square${name}`).value = square;
                // document.getElementById(`cube${name}`).value = cube;
                // document.getElementById('square_a').value = square_a;
                // document.getElementById('square_b').value = square_b;
                // document.getElementById('square_floor').value = square_floor;
                // if (!isNaN(price_for_meter)) {
                    // var total_price = square * price_for_meter
                    // document.getElementById(`price_out${name}`).value = total_price;
                // }
                return square
            } else {
                // document.getElementById('perimeter').value = 'Введите все размеры';
                document.getElementById(`square${name}`).value = 'Введите все размеры';
                document.getElementById(`cube${name}`).value = 'Введите все размеры';
                // document.getElementById('square_a').value = 'Введите все размеры';
                // document.getElementById('square_b').value = 'Введите все размеры';
                // document.getElementById('square_floor').value = 'Введите все размеры';
            }
        }
        
        // Добавляем обработчики событий для полей ввода
        // document.getElementById('width_a').addEventListener('input', calculatePerimeter);
        document.getElementById('width_a').addEventListener('input', (event) => calculatePerimeter('_a'));
        document.getElementById('width_b').addEventListener('input', (event) => calculatePerimeter('_b'));
        document.getElementById('width__floor').addEventListener('input', (event) => calculatePerimeter('__floor'));
        document.getElementById('width_top').addEventListener('input', (event) => calculatePerimeter('_top'));
        // document.getElementById('height_a').addEventListener('input', calculatePerimeter);
        document.getElementById('height_a').addEventListener('input', (event) => calculatePerimeter('_a'));
        document.getElementById('height_b').addEventListener('input', (event) => calculatePerimeter('_b'));
        document.getElementById('height__floor').addEventListener('input', (event) => calculatePerimeter('__floor'));
        document.getElementById('height_top').addEventListener('input', (event) => calculatePerimeter('_top'));
        // document.getElementById('room_size').addEventListener('input', calculatePerimeter);
        // document.getElementById('price_in').addEventListener('input', (event) => calculatePerimeter('_a'));
        
        
        function add_inputs(name, layersCount) {
            var container = document.getElementById(`layers-inputs-container${name}`);
        // console.log(container)
        container.innerHTML = ''; // Очищаем предыдущие поля
        
        // var layersCount = this.value;
        console.log(layersCount)
        
        for (var i = 1; i <= layersCount; i++) {
            var layerDiv = document.createElement('div');
            layerDiv.classList.add('layer-inputs');
            layerDiv.innerHTML = `
            <div class="form-group">
            <label for="wall-${name}-${i}-thickness">Толщина слоя ${i} (мм):</label>
            <input type="number" id="wall-${name}-${i}-thickness" name="wall-${name}-${i}-thickness" step="0.01" required>
            </div>
            <div class="form-group">
            <label for="wall-${name}-${i}-material">Категория слоя ${i}:</label>
            <select id="wall-${name}-${i}-material" name="wall-${name}-${i}-material" style="color: rgb(0, 0, 0)">
            <option value="brick" data-lambda="0.7">Утеплитель</option>
            <option value="concrete" data-lambda="1.1">Металл</option>
            <option value="wood" data-lambda="0.15">Пластик</option>
            <option value="wood" data-lambda="0.15">Газ</option>
            <option value="wood" data-lambda="0.15">Вакум</option>
            </select>
            </div>
            <div class="form-group">
            <label for="wall-${name}-${i}-material1">Материал слоя ${i}:</label>
            <select id="wall-${name}-${i}-material1" name="wall-${name}-${i}-material1" style="color: rgb(0, 0, 0)">
            <option value="knauf" data-lambda="0.035" price="4998" hieght="1000" weight="1000" size="100" count="12">KНАУФ Терм Дача пенопласт 1000*1000*100, 12шт</option>
            <option value="concrete" data-lambda="1.1"></option>
            <option value="wood" data-lambda="0.15"></option>
            <option value="wood" data-lambda="0.15"></option>
            <option value="wood" data-lambda="0.15"></option>
            </select>
            </div>
            `;
            container.appendChild(layerDiv);
            
            document.getElementById(`wall-${name}-${i}-thickness`).addEventListener('change', (event) =>calculateMaterials(name, layersCount, 0));
            document.getElementById(`wall-${name}-${i}-material`).addEventListener('change', (event) =>calculateMaterials(name, layersCount, 0));
            document.getElementById(`wall-${name}-${i}-material1`).addEventListener('change', (event) =>calculateMaterials(name, layersCount, 0));
        }
    }
    // document.getElementById('layers-count_a').addEventListener('change', () => add_inputs('_a', this.value));
    document.getElementById('layers-count_a').addEventListener('change', (event) => add_inputs('_a', event.target.value));
    document.getElementById('layers-count_b').addEventListener('change', (event) => add_inputs('_b', event.target.value));
    document.getElementById('layers-count__floor').addEventListener('change', (event) => add_inputs('__floor', event.target.value));
    document.getElementById('layers-count_top').addEventListener('change', (event) => add_inputs('_top', event.target.value));
    
    function get_all_with() {
        var layersCount = parseInt(document.getElementById('layers-count').value);
        var totalThickness = 0;
        
        for (var i = 1; i <= layersCount; i++) {
            var thicknessInput = document.getElementById(`wall-${i}-thickness`);
            var thicknessValue = parseFloat(thicknessInput.value);
            
            if (!isNaN(thicknessValue)) { // Проверка, что введено числовое значение
                totalThickness += thicknessValue;
            }
        }
        return totalThickness
    }
    $(document).ready(async function() {
    updateTemperature()
    $('#room-params').submit(async function(e) {
        e.preventDefault(); // Предотвратить стандартную отправку формы
        // Показываем комнату
        // Ваши расчеты и обновление данных
        
        // Показываем комнату
        
        // Предполагаем, что вы вызовете функцию plotTemperatureCurve и другие необходимые функции здесь
        var width = $('#width').val() / 1000;
        var height = $('#height').val() / 1000;
        var initialTemp = $('#initial-temp').val();
        // var wallThickness = $('#wall-thickness').val() / 1000;
        var wallThickness = get_all_with() / 1000;
        
        var room_size = $('#room_size').val() / 1000;
        var material = $('#material').find(':selected');
        var time = $('#time').val();
        if (!time) {
            time = 1
        }
        var lambda = material.data('lambda'); // Получаем значение теплопроводности выбранного материала
        
        $('.room').attr('data-wall-thickness', 'Толщина стены: ' + (wallThickness * 1000) + 'мм');
        
        $('.width-dimension').text(width * 1000+ 'мм')
        $('.height-dimension').text(height * 1000+ 'мм')
        $('.temperature').text('Температура:' + initialTemp + '°C')
        if (width > height) {
            $('.room').css('width', '599px');
            $('.room').css('hight', '300px');
        } else {
            $('.room').css('width', '300px');
            $('.room').css('hight', '599px');
        }
        
            border_size = 10
            if (wallThickness <= 1) {
                border_size = 20
            } else if (wallThickness <= 2){
                border_size = 30
            } else if (wallThickness <= 5){
                border_size = 40
            } else {
                border_size = 40
            }
            $('.room').css('border', border_size + 'px solid rgb(187, 140, 0)');
            $('.room').css('display', 'flex');
            
            temp = await getTemperature();
            plotTemperatureCurve(initialTemp, temp, 0.1);
            setInterval(async () => {await updateTemperature()}, 600000);
            
            setInterval(async () => {
                plotTemperatureCurve(25, await getTemperature(), 0.1);
            }, 600000);
            // console.log(temp)
            var temp_into = calc_temp_into(lambda, 0.1, temp, initialTemp);
            $('#temp-into').html('Теплопроводность стенки: ' + temp_into.toFixed(6) + '<br>Считается по формуле: l/w * (t1-t2)<br>l - коэффициент теплопроводимости<br>w - ширина стенки<br>t1 - t2 - разница температур');
            
            resist = updateResistor(wallThickness, lambda)
            // console.log(delta_math(temp, initialTemp), calc_square(height, width, room_size, time * 60, resist));
            heat = updateHeat(delta_math(temp, initialTemp), calc_square(height, width, room_size), time * 60, resist);
            updateTemperatureChange(heat, calc_mass(calc_cube(width, height, room_size)),1.005);
            
        });
        
    });
    
    function calculateInsulationRolls(wallLength, wallHeight, wallThickness, rollLength, rollHeight, rollThickness) {
        
        const wallVolume = wallLength * wallHeight * wallThickness;
        
        const rollVolume = rollLength * rollHeight * rollThickness;
        
        return Math.ceil(wallVolume / rollVolume);
    }
    
    
    function calculateMaterials(name, layersCount, wallArea) {
        var totalCost = 0;
        var totalPackages = 0;
        var totalcube = 0;
        var width = parseFloat(document.getElementById(`width${name}`).value) / 1000;
        var height = parseFloat(document.getElementById(`height${name}`).value) / 1000;
        for (var i = 1; i <= layersCount; i++) {
            wallArea = width * height
            var thicknessElement = parseFloat(document.getElementById(`wall-${name}-${i}-thickness`).value) / 1000;
            var materialElement = document.getElementById(`wall-${name}-${i}-material1`);
            wallArea *= thicknessElement
            // console.log(thicknessElement);
            // console.log(wallArea);
            // var thickness = parseFloat(thicknessElement.value) / 1000; // Конвертируем мм в метры
            var materialOption = materialElement.options[materialElement.selectedIndex];
            // var lambda = parseFloat(materialOption.getAttribute('data-lambda'));
            var pricePerPackage = parseFloat(materialOption.getAttribute('price'));
            var packageCube = parseFloat(materialOption.getAttribute('hieght'))/ 1000 * parseFloat(materialOption.getAttribute('weight')) / 1000 * parseFloat(materialOption.getAttribute('size')) / 1000 * parseFloat(materialOption.getAttribute('count'));
            var packagesNeeded = Math.ceil(wallArea / packageCube);
            
            totalcube += wallArea
            totalCost += packagesNeeded * pricePerPackage;
            totalPackages += packagesNeeded;
        }
    
    document.getElementById(`count${name}`).value = totalPackages;
    document.getElementById(`price_out${name}`).value = totalCost;
    document.getElementById(`cube${name}`).value = totalcube;
    // try {
    setAllRes();
    // } catch {
    //     console.log("Cant");
    // };
    // document.getElementById('square_a').value = 'Введите все размеры';
    // return { totalCost, totalPackages };
}

function setAllRes() {
    // var square, cube, cost = count_all_res();
    var {total_square: square, total_cube: cube, total_cost: cost, air_cube: air} = count_all_res();
    document.getElementById(`square`).value = square;
    document.getElementById(`cube_wall`).value = cube;
    document.getElementById(`price_out`).value = cost;
    document.getElementById(`cube_air`).value = air;
    
}

function count_all_res() {
    var all_names = ['_a', '_b', "__floor", "_top"];
    var total_square = 0;
    var total_cube = 0;
    var total_cost = 0;
    all_names.forEach((element) => {
        total_square += calculateSq(element);
        total_cube += calculateCube(element);
        total_cost += calculateCost(element);
    }
    );
    air_cube = calculate_main_cube() - total_cube;
    return {total_square, total_cube, total_cost, air_cube};
}

function calculateCube(name) {
    return parseFloat(count_of_layers = document.getElementById(`cube${name}`).value)
}
function calculateSq(name) {
    return parseFloat(count_of_layers = document.getElementById(`square${name}`).value)
}
function calculateCost(name) {
    return parseFloat(count_of_layers = document.getElementById(`price_out${name}`).value)
}

function calculate_main_cube() {
    a = parseFloat(document.getElementById("width_a").value) / 1000;
    b = parseFloat(document.getElementById("height_a").value) / 1000;
    c = parseFloat(document.getElementById("width_b").value) / 1000;
    return a * b * c
}