/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/06.2_enums_with_arrays.yml
 *   Object: EnumsWithArrays
 *   Template: qt6/service_header.j2
 */
#pragma once
#include <QObject>
#include <qqmlintegration.h>
#include <QDBusAbstractAdaptor>
#include <QDBusMessage>
#include "EnumsWithArraysInterface.hpp"

namespace gen::enums {

/**
 * @brief D-Bus adaptor for the EnumsWithArrays interface.
 */
class EnumsWithArraysInterfaceAdaptor : public QDBusAbstractAdaptor {
    Q_OBJECT
    Q_CLASSINFO("D-Bus Interface", "com.yarpc.testservice.enumsWithArrays")
    /**
     * @brief a property
     */
    Q_PROPERTY(QList<int> EnumProperty READ getEnumProperty WRITE setEnumProperty )

public:
    EnumsWithArraysInterfaceAdaptor(EnumsWithArraysInterface* iface, QObject* parent = nullptr);
public slots:
    /**
     * @brief a simple method with one argument
     *
     * @param color a color
     * @param _message The D-Bus message object
     *
     * @returns another color
     */
    QList<int> EnumMethod(
        QList<int> color,
        const QDBusMessage &_message
    );
signals:
    /**
     * @brief a simple signal with one argument
     *
     * @param color a color
     *
     */
    void EnumSignal(
        QList<int> color
    );
private:
    QList<int> getEnumProperty() const;
    void setEnumProperty(const QList<int> &value );
    EnumsWithArraysInterface* m_iface;
};

}