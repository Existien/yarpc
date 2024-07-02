/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/03_structs.yml
 *   Object: Structs
 *   Template: qt6/service_header.j2
 */
#pragma once
#include <QObject>
#include <qqmlintegration.h>
#include <QDBusMessage>
#include <QVariant>
#include "DBusError.hpp"
#include "SimpleStruct.hpp"
#include "Item.hpp"
namespace gen::structs {

/**
 * @brief The arguments passed during a SendStruct call.
 */
class SendStructArgs {
    Q_GADGET
    /**
     * @brief the SimpleStruct to send
     */
    Q_PROPERTY(SimpleStruct simpleStruct MEMBER simpleStruct)
public:
    SimpleStruct simpleStruct;
};

/**
 * @brief A pending reply to a SendStruct call.
 *
 * Use the sendReply or sendError methods to send the pending reply.
 */
class SendStructPendingReply : public QObject {
    Q_OBJECT
    QML_UNCREATABLE("")
    QML_ELEMENT
public:
    SendStructPendingReply(QDBusMessage call, QObject *parent);

    /**
     * @brief Send a reply to the pending call.
     *
     * @param reply the return value of the call
     */
    void sendReply(
        const SimpleStruct &reply
    );
public slots:
    /**
     * @brief Returns the arguments passed during a SendStruct call.
     *
     * @returns the arguments of the call
     */
    SendStructArgs args();

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
     *   (needs to be in the form of a D-Bus URI, e.g. "com.yarpc.testservice.structs.OutOfCheeseError")
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
    SendStructArgs m_args;
};


/**
 * @brief A interface with structures
 */
class StructsInterface : public QObject {
    Q_OBJECT
    QML_ELEMENT
    QML_SINGLETON

    /** @brief Whether the interface is registered and connected */
    Q_PROPERTY(bool connected READ getConnected NOTIFY connectedChanged )

    /**
     * @brief a property for a simple struct
     */
    Q_PROPERTY(QVariant simple READ getVariantSimple WRITE setVariantSimple NOTIFY simpleChanged)

public:
    StructsInterface(QObject* parent = nullptr);

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
     * @brief Handler for SendStruct D-Bus calls.
     *
     * @param call the D-Bus call object
     */
    void handleSendStructCalled(QDBusMessage call);




    /**
     * @brief Getter for the Simple property.
     *
     * @returns the current value of the property
     */
    SimpleStruct getSimple() const;

    /**
     * @brief Setter for the Simple property.
     *
     * @param value the new value of the property
     */
    void setSimple(const SimpleStruct &value );


    /**
     * @brief a signal with a struct as args
     *
     * @param simpleStruct the SimpleStruct
     * @param totalCosts the total costs
     */
    void EmitStructReceived(
        SimpleStruct simpleStruct,
        double totalCosts
    );


public slots:
    /** @brief Registeres and connects the interface. */
    void connect();

    /** @brief Unregisteres and disconnects the interface. */
    void disconnect();

    /**
     * @brief a signal with a struct as args
     *
     * @param simpleStruct the SimpleStruct
     * @param totalCosts the total costs
     */
    void EmitStructReceived(
        QVariant simpleStruct,
        QVariant totalCosts
    );


private:

    /**
     * @brief Getter for the Simple property as variant.
     *
     * @returns the current value of the property as variant
     */
    QVariant getVariantSimple() const;

    /**
     * @brief Setter for the Simple property as variant.
     *
     * @param value the new value of the property wrapped in a variant
     */
    void setVariantSimple(QVariant value );


signals:
    /**
     * @brief Emitted when the connection status changes.
     */
    void connectedChanged();

    /**
     * @brief Emitted when a client calls the SendStruct method.
     *
     * @param reply the reply object containing the call arguments and means to reply
     */
    void sendStructCalled(SendStructPendingReply* reply);

    /**
     * @brief Emitted when a client tries to set the Simple property.
     *
     * @param value the new value of the property
     */
    void propertySimpleSet(SimpleStruct value);

    /**
     * @brief Emitted when the value of the Simple property changes.
     */
    void simpleChanged();

private:
    void emitPropertiesChangedSignal(const QVariantMap &changedProperties);
    SimpleStruct m_Simple = {};
};

}