/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/02.1_with_args.yml
 *   Object: WithArgs
 *   Template: qt6/service_header.j2
 */
#pragma once
#include <QObject>
#include <qqmlintegration.h>
#include <QDBusAbstractAdaptor>
#include <QDBusMessage>
#include "WithArgsInterface.hpp"

namespace gen::with_args {

/**
 * @brief D-Bus adaptor for the WithArgs interface.
 */
class WithArgsInterfaceAdaptor : public QDBusAbstractAdaptor {
    Q_OBJECT
    Q_CLASSINFO("D-Bus Interface", "com.yarpc.testservice.withArgs")
    /**
     * @brief the speed
     *   in m/s
     */
    Q_PROPERTY(double Speed READ getSpeed WRITE setSpeed )

    /**
     * @brief the distance to travel in m
     */
    Q_PROPERTY(uint Distance READ getDistance WRITE setDistance )

    /**
     * @brief the time until the distance is covered at the current speed
     */
    Q_PROPERTY(double Duration READ getDuration )

public:
    WithArgsInterfaceAdaptor(WithArgsInterface* iface, QObject* parent = nullptr);
public slots:
    /**
     * @brief a simple method with one argument
     *
     * @param message The message
     * @param _message The D-Bus message object
     *
     */
    void Notify(
        QString message,
        const QDBusMessage &_message
    );
    /**
     * @brief a simple method
     *   with args and return value
     *
     * @param item The
     *   item
     * @param amount a amount ordered
     * @param pricePerItem the price per item
     * @param _message The D-Bus message object
     *
     * @returns the
     *   total price
     */
    double Order(
        QString item,
        uint amount,
        double pricePerItem,
        const QDBusMessage &_message
    );
signals:
    /**
     * @brief a simple signal with one argument
     *
     * @param message The message
     *
     */
    void Notified(
        QString message
    );
    /**
     * @brief a simple signal with
     *   multiple arguments
     *
     * @param item The item
     * @param amount a amount
     *   ordered
     * @param pricePerItem the price per item
     *
     */
    void OrderReceived(
        QString item,
        uint amount,
        double pricePerItem
    );
private:
    double getSpeed() const;
    void setSpeed(const double &value );
    uint getDistance() const;
    void setDistance(const uint &value );
    double getDuration() const;
    WithArgsInterface* m_iface;
};

}