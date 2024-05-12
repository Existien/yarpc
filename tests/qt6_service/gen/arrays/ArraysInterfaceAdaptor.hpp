/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/04.1_arrays.yml
 *   Object: Arrays
 *   Template: qt6/service_header.j2
 */
#pragma once
#include <QObject>
#include <qqmlintegration.h>
#include <QDBusAbstractAdaptor>
#include <QDBusMessage>
#include "ArraysInterface.hpp"

namespace gen::arrays {

/**
 * @brief D-Bus adaptor for the Arrays interface.
 */
class ArraysInterfaceAdaptor : public QDBusAbstractAdaptor {
    Q_OBJECT
    Q_CLASSINFO("D-Bus Interface", "com.yarpc.testservice.arrays")
    /**
     * @brief a simple property
     */
    Q_PROPERTY(QList<$1> ArrayProperty READ getArrayProperty WRITE setArrayProperty )

public:
    ArraysInterfaceAdaptor(ArraysInterface* iface, QObject* parent = nullptr);
public slots:
    /**
     * @brief a simple method with one argument
     *
     * @param numbers Some numbers
     * @param _message The D-Bus message object
     *
     * @returns normalized numbers
     */
    QList<$1> ArrayMethod(
        QList<$1> numbers,
        const QDBusMessage &_message
    );
signals:
    /**
     * @brief a simple signal with one argument
     *
     * @param numbers normalized numbers
     *
     */
    void ArraySignal(
        QList<$1> numbers
    );
private:
    QList<$1> getArrayProperty() const;
    void setArrayProperty(const QList<$1> &value );
    ArraysInterface* m_iface;
};

}