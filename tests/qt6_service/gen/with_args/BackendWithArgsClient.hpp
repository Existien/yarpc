/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/02.1_with_args.yml
 *   Object: WithArgs
 *   Template: qt6/client_header.j2
 */
#pragma once
#include <QObject>
#include <qqmlintegration.h>
#include <QDBusMessage>
#include <QDBusServiceWatcher>
#include <QDBusPendingCallWatcher>
#include <QVariant>
#include "DBusError.hpp"
#include "types.hpp"
namespace gen::with_args {

namespace BackendWithArgsClientUtils {

/**
 * @brief Pending call object for the Notify method calls.
 */
class NotifyPendingCall : public QObject {
    Q_OBJECT
    QML_UNCREATABLE("")
    QML_ELEMENT
public:
    NotifyPendingCall(QDBusPendingCall pendingCall, QObject *parent);
signals:
    /**
     * @brief Emitted when an Notify call returns.
     */
    void finished();

    /**
     * @brief Emitted when an error ocurred during an Notify call.
     *
     * @param error the error
     */
    void error(DBusError error);
private slots:
    void callFinished(QDBusPendingCallWatcher *watcher);
private:
    QDBusPendingCallWatcher m_watcher;
};

/**
 * @brief Pending call object for the Order method calls.
 */
class OrderPendingCall : public QObject {
    Q_OBJECT
    QML_UNCREATABLE("")
    QML_ELEMENT
public:
    OrderPendingCall(QDBusPendingCall pendingCall, QObject *parent);
signals:
    /**
     * @brief Emitted when an Order call returns.
     *
     * @param the
     *   total price
     */
    void finished(const double &reply);

    /**
     * @brief Emitted when an error ocurred during an Order call.
     *
     * @param error the error
     */
    void error(DBusError error);
private slots:
    void callFinished(QDBusPendingCallWatcher *watcher);
private:
    QDBusPendingCallWatcher m_watcher;
};

}

/**
 * D-Bus client for the com.yarpc.backend.withArgs D-Bus interface
 */
class BackendWithArgsClient : public QObject {
    Q_OBJECT
    QML_ELEMENT
    /**
     * @brief Whether the client is connected.
     */
    Q_PROPERTY(bool connected READ getConnected NOTIFY connectedChanged)
    /**
     * @brief the speed
     *   in m/s
     */
    Q_PROPERTY(QVariant speed READ getVariantSpeed WRITE setVariantSpeed NOTIFY speedChanged)

    /**
     * @brief the distance to travel in m
     */
    Q_PROPERTY(QVariant distance READ getVariantDistance WRITE setVariantDistance NOTIFY distanceChanged)

    /**
     * @brief the time until the distance is covered at the current speed
     */
    Q_PROPERTY(QVariant duration READ getVariantDuration NOTIFY durationChanged)

public:
    BackendWithArgsClient(QObject* parent = nullptr);

    /**
     * @brief a simple method with one argument
     *
     * @param message The message
     *
     * @returns Pending call object with finished signal containing the reply.
     */
    BackendWithArgsClientUtils::NotifyPendingCall* Notify(
        QString message
    );

    /**
     * @brief a simple method
     *   with args and return value
     *
     * @param item The
     *   item
     * @param amount a amount ordered
     * @param pricePerItem the price per item
     *
     * @returns Pending call object with finished signal containing the reply.
     */
    BackendWithArgsClientUtils::OrderPendingCall* Order(
        QString item,
        uint amount,
        double pricePerItem
    );

    /**
     * @brief Getter for the Speed property.
     *
     * @returns the current value of the property
     *
     * the speed
     * in m/s
     */
    double getSpeed() const;

    /**
     * @brief Setter for the Speed property.
     *
     * @param newValue the new value of the property
     *
     * the speed
     * in m/s
     */
    void setSpeed(const double &newValue);

    /**
     * @brief Getter for the Distance property.
     *
     * @returns the current value of the property
     *
     * the distance to travel in m
     */
    uint getDistance() const;

    /**
     * @brief Setter for the Distance property.
     *
     * @param newValue the new value of the property
     *
     * the distance to travel in m
     */
    void setDistance(const uint &newValue);

    /**
     * @brief Getter for the Duration property.
     *
     * @returns the current value of the property
     *
     * the time until the distance is covered at the current speed
     */
    double getDuration() const;

public slots:
    /**
     * @brief Returns whether the target service is available.
     *
     * @returns Whether the target service is available.
     */
    bool getConnected() const;

    /**
     * @brief Returns a map containing the current values of all properties.
     *
     * @returns a map containing the current values of all properties
     */
    QVariantMap getAllProperties() const;

    /**
     * @brief a simple method with one argument
     *
     * @param message The message
     *
     * @returns Pending call object with finished signal containing the reply.
     */
    BackendWithArgsClientUtils::NotifyPendingCall* Notify(
        QVariant message
    );

    /**
     * @brief a simple method
     *   with args and return value
     *
     * @param item The
     *   item
     * @param amount a amount ordered
     * @param pricePerItem the price per item
     *
     * @returns Pending call object with finished signal containing the reply.
     */
    BackendWithArgsClientUtils::OrderPendingCall* Order(
        QVariant item,
        QVariant amount,
        QVariant pricePerItem
    );

signals:
    /**
     * @brief Emitted when the connected property changes.
     */
    void connectedChanged();

    /**
     * @brief a simple signal with one argument
     *
     * @param message The message
     */
    void notifiedReceived(
        QVariant message
    );

    /**
     * @brief a simple signal with
     *   multiple arguments
     *
     * @param item The item
     * @param amount a amount
     *   ordered
     * @param pricePerItem the price per item
     */
    void orderReceivedReceived(
        QVariant item,
        QVariant amount,
        QVariant pricePerItem
    );

    /**
     * @brief Changed signal for the Speed property.
     *
     * the speed
     * in m/s
     */
    void speedChanged();

    /**
     * @brief Changed signal for the Distance property.
     *
     * the distance to travel in m
     */
    void distanceChanged();

    /**
     * @brief Changed signal for the Duration property.
     *
     * the time until the distance is covered at the current speed
     */
    void durationChanged();

private slots:
    void connectedHandler(const QString& service);
    void disconnectedHandler(const QString& service);
    void propertiesChangedHandler(QString interface, QVariantMap changes, QStringList);
    void NotifiedDBusHandler(QDBusMessage content);
    void OrderReceivedDBusHandler(QDBusMessage content);

    /**
     * @brief Getter for the Speed property as variant.
     *
     * @returns the current value of the property as variant
     *
     * the speed
     * in m/s
     */
    QVariant getVariantSpeed() const;

    /**
     * @brief Setter for the Speed property as variant.
     *
     * @param newValue the new value of the property wrapped in a variant
     *
     * the speed
     * in m/s
     */
    void setVariantSpeed(QVariant newValue);

    /**
     * @brief Getter for the Distance property as variant.
     *
     * @returns the current value of the property as variant
     *
     * the distance to travel in m
     */
    QVariant getVariantDistance() const;

    /**
     * @brief Setter for the Distance property as variant.
     *
     * @param newValue the new value of the property wrapped in a variant
     *
     * the distance to travel in m
     */
    void setVariantDistance(QVariant newValue);

    /**
     * @brief Getter for the Duration property as variant.
     *
     * @returns the current value of the property as variant
     *
     * the time until the distance is covered at the current speed
     */
    QVariant getVariantDuration() const;
private:
    bool m_connected = false;
    QDBusServiceWatcher m_watcher;
};

}