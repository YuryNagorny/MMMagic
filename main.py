<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1140</width>
    <height>720</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QVBoxLayout" name="verticalLayout">
    <item>
     <layout class="QHBoxLayout" name="horizontalLayout">
      <item>
       <widget class="QWidget" name="start" native="true">
        <widget class="QWidget" name="app_id_window" native="true">
         <property name="geometry">
          <rect>
           <x>300</x>
           <y>90</y>
           <width>521</width>
           <height>501</height>
          </rect>
         </property>
         <layout class="QVBoxLayout" name="verticalLayout_3">
          <item>
           <widget class="QLabel" name="label_16">
            <property name="font">
             <font>
              <pointsize>14</pointsize>
             </font>
            </property>
            <property name="text">
             <string>Введите все необходимые данные </string>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QLabel" name="label_7">
            <property name="font">
             <font>
              <pointsize>10</pointsize>
             </font>
            </property>
            <property name="text">
             <string>Введите id приложения:</string>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QLineEdit" name="Enter_ID"/>
          </item>
          <item>
           <widget class="QPushButton" name="Get_Code">
            <property name="font">
             <font>
              <pointsize>10</pointsize>
             </font>
            </property>
            <property name="text">
             <string>Получить код доступа</string>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QLabel" name="label_11">
            <property name="font">
             <font>
              <pointsize>10</pointsize>
             </font>
            </property>
            <property name="text">
             <string>Ваша ссылка на код доступа:</string>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QLineEdit" name="Code_Link"/>
          </item>
          <item>
           <widget class="QLabel" name="label_12">
            <property name="styleSheet">
             <string notr="true">QLabel {
  color: red;
  font-family: Helvetica, Arial, sans-serif;
}</string>
            </property>
            <property name="text">
             <string/>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QLabel" name="label_13">
            <property name="font">
             <font>
              <pointsize>10</pointsize>
             </font>
            </property>
            <property name="text">
             <string>Введите код доступа, полученный по ссылке:</string>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QLineEdit" name="Enter_Code"/>
          </item>
          <item>
           <widget class="QLabel" name="label_14">
            <property name="font">
             <font>
              <pointsize>10</pointsize>
             </font>
            </property>
            <property name="text">
             <string>Введите защищенный ключ:</string>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QLineEdit" name="Enter_Protect"/>
          </item>
          <item>
           <widget class="QPushButton" name="Continue">
            <property name="font">
             <font>
              <pointsize>10</pointsize>
             </font>
            </property>
            <property name="text">
             <string>Продолжить</string>
            </property>
           </widget>
          </item>
         </layout>
        </widget>
       </widget>
      </item>
      <item>
       <widget class="QWidget" name="menu" native="true">
        <widget class="QWidget" name="widget_3" native="true">
         <property name="geometry">
          <rect>
           <x>-300</x>
           <y>130</y>
           <width>591</width>
           <height>401</height>
          </rect>
         </property>
         <layout class="QVBoxLayout" name="verticalLayout_4">
          <item>
           <widget class="QLabel" name="label_15">
            <property name="font">
             <font>
              <pointsize>16</pointsize>
             </font>
            </property>
            <property name="text">
             <string>Добро пожаловать в VK Features!</string>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QPushButton" name="Album">
            <property name="font">
             <font>
              <pointsize>12</pointsize>
             </font>
            </property>
            <property name="text">
             <string>Загрузить фотоальбом</string>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QPushButton" name="Del_Ban_Friends">
            <property name="font">
             <font>
              <pointsize>12</pointsize>
             </font>
            </property>
            <property name="text">
             <string>Удалить заблокированных друзей</string>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QPushButton" name="Del_AFK_Friends">
            <property name="font">
             <font>
              <pointsize>12</pointsize>
             </font>
            </property>
            <property name="text">
             <string>Удалить друзей, которые были в сети более 1 года назад</string>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QPushButton" name="Download_Photo">
            <property name="font">
             <font>
              <pointsize>12</pointsize>
             </font>
            </property>
            <property name="text">
             <string>Загрузить фотографии со стены</string>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QPushButton" name="Del_Publics">
            <property name="font">
             <font>
              <pointsize>12</pointsize>
             </font>
            </property>
            <property name="text">
             <string>Удалить группы, не добавляющие записи более 1 года</string>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QPushButton" name="Del_Noti">
            <property name="font">
             <font>
              <pointsize>12</pointsize>
             </font>
            </property>
            <property name="text">
             <string>Очистить список уведомлений </string>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QPushButton" name="Establish_Status">
            <property name="font">
             <font>
              <pointsize>12</pointsize>
             </font>
            </property>
            <property name="text">
             <string>Установить статус своей страницы</string>
            </property>
           </widget>
          </item>
         </layout>
        </widget>
       </widget>
      </item>
     </layout>
    </item>
   </layout>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>

