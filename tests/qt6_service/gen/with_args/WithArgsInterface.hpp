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
#include <QDBusMessage>
#include <QVariant>
#include "DBusError.hpp"
#include "types.hpp"
namespace gen::with_args {

/**
 * @brief The arguments passed during a Notify call.
 */
class NotifyArgs {
    Q_GADGET
    /**
     * @brief The message
     */
    Q_PROPERTY(QString message MEMBER message)
public:
    QString message;
};

/**
 * @brief A pending reply to a Notify call.
 *
 * Use the sendReply or sendError methods to send the pending reply.
 */
class NotifyPendingReply : public QObject {
    Q_OBJECT
    QML_UNCREATABLE("")
    QML_ELEMENT
public:
    NotifyPendingReply(QDBusMessage call, QObject *parent);

public slots:
    /**
     * @brief Returns the arguments passed during a Notify call.
     *
     * @returns the arguments of the call
     */
    NotifyArgs args();

    /**
     * @brief Send a reply to the pending call.
     *
     * @param reply the return value of the call
     */
    void sendReply(
    );

    /**
     * @brief Send an error in reply to the pending call.
     *
     * @param name the name of the error
     *   (needs to be in the form of a D-Bus URI, e.g. "com.yarpc.testservice.withArgs.OutOfCheeseError")
     * @param message the error message
     */
    void sendError(const QString &name, const QString &message);

    /**
     * @brief Send an error in reply to the pending call.
     *
     * @param error the D-Bus error to send
     */
    void sendError(const DBusError &error);
private:
    QDBusMessage m_call;
    NotifyArgs m_args;
};

/**
 * @brief The arguments passed during a Order call.
 */
class OrderArgs {
    Q_GADGET
    /**
     * @brief The
     *   item
     */
    Q_PROPERTY(QString item MEMBER item)
    /**
     * @brief a amount ordered
     */
    Q_PROPERTY(uint amount MEMBER amount)
    /**
     * @brief the price per item
     */
    Q_PROPERTY(double pricePerItem MEMBER pricePerItem)
public:
    QString item;
    uint amount;
    double pricePerItem;
};

/**
 * @brief A pending reply to a Order call.
 *
 * Use the sendReply or sendError methods to send the pending reply.
 */
class OrderPendingReply : public QObject {
    Q_OBJECT
    QML_UNCREATABLE("")
    QML_ELEMENT
public:
    OrderPendingReply(QDBusMessage call, QObject *parent);

    /**
     * @brief Send a reply to the pending call.
     *
     * @param reply the return value of the call
     */
    void sendReply(
        const double &reply
    );
public slots:
    /**
     * @brief Returns the arguments passed during a Order call.
     *
     * @returns the arguments of the call
     */
    OrderArgs args();

    /**
     * @brief Send a reply to the pending call.
     *
     * @param reply the return value of the call
     */
    void sendReply(
        QVariant reply
    );

    /**
     * @brief Send an error in reply to the pending call.
     *
     * @param name the name of the error
     *   (needs to be in the form of a D-Bus URI, e.g. "com.yarpc.testservice.withArgs.OutOfCheeseError")
     * @param message the error message
     */
    void sendError(const QString &name, const QString &message);

    /**
     * @brief Send an error in reply to the pending call.
     *
     * @param error the D-Bus error to send
     */
    void sendError(const DBusError &error);
private:
    QDBusMessage m_call;
    OrderArgs m_args;
};


/**
 * @brief A interface using only primitive types
 *   
 *   And some elaborate docstring
 */
class WithArgsInterface : public QObject {
    Q_OBJECT
    QML_ELEMENT
    QML_SINGLETON

    /** @brief Whether the interface is registered and connected */
    Q_PROPERTY(bool connected READ getConnected NOTIFY connectedChanged )

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
    Q_PROPERTY(QVariant duration READ getVariantDuration WRITE setVariantDuration NOTIFY durationChanged)

public:
    WithArgsInterface(QObject* parent = nullptr);

    /**
     * @brief Finishes a pending call by sending a reply.
     *
     * @param reply the reply to send
     */
    void finishCall(const QDBusMessage &reply);

    /**
     * @brief Returns whether the interface is registered and connected
     *
     * @returns whether the interface is registered and connected
     */
    bool getConnected() const;



    /**
     * @brief Handler for Notify D-Bus calls.
     *
     * @param call the D-Bus call object
     */
    void handleNotifyCalled(QDBusMessage call);


    /**
     * @brief Handler for Order D-Bus calls.
     *
     * @param call the D-Bus call object
     */
    void handleOrderCalled(QDBusMessage call);



    /**
     * @brief Getter for the Speed property.
     *
     * @returns the current value of the property
     */
    double getSpeed() const;

    /**
     * @brief Setter for the Speed property.
     *
     * @param value the new value of the property
     */
    void setSpeed(const double &value );


    /**
     * @brief Getter for the Distance property.
     *
     * @returns the current value of the property
     */
    uint getDistance() const;

    /**
     * @brief Setter for the Distance property.
     *
     * @param value the new value of the property
     */
    void setDistance(const uint &value );


    /**
     * @brief Getter for the Duration property.
     *
     * @returns the current value of the property
     */
    double getDuration() const;

    /**
     * @brief Setter for the Duration property.
     *
     * @param value the new value of the property
     */
    void setDuration(const double &value );


    /**
     * @brief a simple signal with one argument
     *
     * @param message The message
     */
    void EmitNotified(
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
     */
    void EmitOrderReceived(
        QString item,
        uint amount,
        double pricePerItem
    );


public slots:
    /** @brief Registeres and connects the interface. */
    void connect();

    /** @brief Unregisteres and disconnects the interface. */
    void disconnect();

    /**
     * @brief a simple signal with one argument
     *
     * @param message The message
     */
    void EmitNotified(
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
    void EmitOrderReceived(
        QVariant item,
        QVariant amount,
        QVariant pricePerItem
    );


private:

    /**
     * @brief Getter for the Speed property as variant.
     *
     * @returns the current value of the property as variant
     */
    QVariant getVariantSpeed() const;

    /**
     * @brief Setter for the Speed property as variant.
     *
     * @param value the new value of the property wrapped in a variant
     */
    void setVariantSpeed(QVariant value );

    /**
     * @brief Getter for the Distance property as variant.
     *
     * @returns the current value of the property as variant
     */
    QVariant getVariantDistance() const;

    /**
     * @brief Setter for the Distance property as variant.
     *
     * @param value the new value of the property wrapped in a variant
     */
    void setVariantDistance(QVariant value );

    /**
     * @brief Getter for the Duration property as variant.
     *
     * @returns the current value of the property as variant
     */
    QVariant getVariantDuration() const;

    /**
     * @brief Setter for the Duration property as variant.
     *
     * @param value the new value of the property wrapped in a variant
     */
    void setVariantDuration(QVariant value );


signals:
    /**
     * @brief Emitted when the connection status changes.
     */
    void connectedChanged();

    /**
     * @brief Emitted when a client calls the Notify method.
     *
     * @param reply the reply object containing the call arguments and means to reply
     */
    void notifyCalled(NotifyPendingReply* reply);

    /**
     * @brief Emitted when a client calls the Order method.
     *
     * @param reply the reply object containing the call arguments and means to reply
     */
    void orderCalled(OrderPendingReply* reply);

    /**
     * @brief Emitted when a client tries to set the Speed property.
     *
     * @param value the new value of the property
     */
    void propertySpeedSet(double value);

    /**
     * @brief Emitted when the value of the Speed property changes.
     */
    void speedChanged();
    /**
     * @brief Emitted when a client tries to set the Distance property.
     *
     * @param value the new value of the property
     */
    void propertyDistanceSet(uint value);

    /**
     * @brief Emitted when the value of the Distance property changes.
     */
    void distanceChanged();
    /**
     * @brief Emitted when a client tries to set the Duration property.
     *
     * @param value the new value of the property
     */
    void propertyDurationSet(double value);

    /**
     * @brief Emitted when the value of the Duration property changes.
     */
    void durationChanged();

private:
    void emitPropertiesChangedSignal(const QVariantMap &changedProperties);
    double m_Speed = {};
    uint m_Distance = {};
    double m_Duration = {};
};

}