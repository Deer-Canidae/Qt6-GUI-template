#pragma once

#include <QBoxLayout>
#include <QMenuBar>
#include <QtWidgets/QMainWindow>

class QtWidgetsApplication1 : public QMainWindow {
  Q_OBJECT

public:
  QtWidgetsApplication1(QWidget *parent = nullptr);
  ~QtWidgetsApplication1();
};
