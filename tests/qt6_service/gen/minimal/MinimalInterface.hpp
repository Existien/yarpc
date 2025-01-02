/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/01_minimal.yml
 *   Object: Minimal
 *   Template: qt6/service_header.j2
 */
#pragma once
#include <QObject>
#include <qqmlintegration.h>
#include <QDBusMessage>
#include <QVariant>
#include "DBusError.hpp"
#include "types.hpp"
namespace gen::minimal {

/**
 * @brief The arguments passed during a Bump call.
 */
class BumpArgs {
    Q_GADGET
public:
};

/**
 * @brief A pending reply to a Bump call.
 *
 * Use the sendReply or sendError methods to send the pending reply.
 */
class BumpPendingReply : public QObject {
    Q_OBJECT
    QML_UNCREATABLE("")
    QML_ELEMENT
public:
    BumpPendingReply(QDBusMessage call, QObject *parent);

public slots:
    /**
     * @brief Returns the arguments passed during a Bump call.
     *
     * @returns the arguments of the call
     */
    BumpArgs args();

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
     *   (needs to be in the form of a D-Bus URI, e.g. "com.yarpc.testservice.minimal.OutOfCheeseError")
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
    BumpArgs m_args;
};


/**
 * @brief A interface using signals and methods without args
 */
class MinimalInterface : public QObject {
    Q_OBJECT
    QML_ELEMENT
    QML_SINGLETON

    /** @brief Whether the interface is registered and connected */
    Q_PROPERTY(bool connected READ getConnected NOTIFY connectedChanged )

public:
    MinimalInterface(QObject* parent = nullptr);

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
     * @brief Handler for Bump D-Bus calls.
     *
     * @param call the D-Bus call object
     */
    void handleBumpCalled(QDBusMessage call);



public slots:
    /** @brief Registeres and connects the interface. */
    void connect();

    /** @brief Unregisteres and disconnects the interface. */
    void disconnect();

    /**
     * @brief a simple signal without arguments
     */
    void EmitBumped(
    );


private:


signals:
    /**
     * @brief Emitted when the connection status changes.
     */
    void connectedChanged();

    /**
     * @brief Emitted when a client calls the Bump method.
     *
     * @param reply the reply object containing the call arguments and means to reply
     */
    void bumpCalled(BumpPendingReply* reply);


private:
    void emitPropertiesChangedSignal(const QVariantMap &changedProperties);
};

}