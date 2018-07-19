# Инструкция по установке данного проекта на свобственную версию Ubuntu

Данная инструкция подскажет как установить необходимые компоненты для работы 
с виртуальным роботом. Представленные ниже команды рекомендуется выполнять 
последовательно.

### Установка ROS и Gazebo

Ниже представлен перевод 
[данной](http://wiki.ros.org/kinetic/Installation/Ubuntu)
инструкции.

1. Установка "sources.list"
```
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
```

2. Установка ключей
```
sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116
```

3. Установка дистрибутива
```
sudo apt-get update
sudo apt-get install ros-kinetic-desktop-full
```

4. Инициализация инструмента командной строки 
для установки системных зависимостей (rosdep).
```
sudo rosdep init
rosdep update
```

5. Настройка среды
```
echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

6. Установка зависимостей для создания пакетов
```
sudo apt-get install python-rosinstall python-rosinstall-generator python-wstool build-essential
```

## Установка инструментов командной строки catkin

Ниже представлен перевод 
[данной](http://catkin-tools.readthedocs.io/en/latest/installing.html)
инструкции.


1. Установка хранилищ ROS, содержащих .dev для catkin_tool
```
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu `lsb_release -sc` main" > /etc/apt/sources.list.d/ros-latest.list'
wget http://packages.ros.org/ros.key -O - | sudo apt-key add -
```

2. После установки хранилищ ROS следует установить catkin_tool
```
sudo apt-get update
sudo apt-get install python-catkin-tools
```

## Установка рабочего пространства ROS

Ниже представлен перевод 
[данной](http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment)
инструкции.

1. Cоздание рабочего пространства catkin
```
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/
catkin_make
```

2. Настройка среды
```
echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

## Установка робототехнического окружения

Для установки необходимого окружения для работы с виртуальным роботом
рекомендуется выполнить следующие команды:
```
cd ~/catkin_ws/src/
git clone https://github.com/hircumg/pioneer3dx_robot.git
git clone https://github.com/hircumg/robot_library.git
cd ..
catkin_make
```

## Работа с установленным проектом

Для начала работы с установленным проектом рекомендуется вернуться к файлу
[README](README.md)