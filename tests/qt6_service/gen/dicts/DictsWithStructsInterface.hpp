/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/05.2_dictionaries_with_structs.yml
 *   Object: DictsWithStructs
 *   Template: qt6/service_header.j2
 */
#pragma once
#include <QObject>
#include <qqmlintegration.h>
#include <QDBusMessage>
#include "DBusError.hpp"
namespace gen::dicts {

/**
 * @brief The arguments passed during a DictsStructMethod call.
 */
class DictsStructMethodArgs {
    Q_GADGET
    /**
     * @brief Some numbers
     */
    Q_PROPERTY(QMap<$1, $2> numbers MEMBER numbers)
public:
    QMap<$1, $2> numbers;
};

/**
 * @brief A pending reply to a DictsStructMethod call.
 *
 * Use the sendReply or sendError methods to send the pending reply.
 */
class DictsStructMethodPendingReply : public QObject {
    Q_OBJECT
    QML_UNCREATABLE("")
    QML_ELEMENT
public:
    DictsStructMethodPendingReply(QDBusMessage call, QObject *parent);
public slots:
    /**
     * @brief Returns the arguments passed during a DictsStructMethod call.
     *
     * @returns the arguments of the call
     */
    DictsStructMethodArgs args();

    /**
     * @brief Send a reply to the pending call.
     *
     * @param reply the return value of the call
     */
    void sendReply(
        const QMap<$1, $2> &reply
    );

    /**
     * @brief Send an error in reply to the pending call.
     *
     * @param name the name of the error
     *   (needs to be in the form of a D-Bus URI, e.g. "com.yarpc.testservice.dictsWithStructs.OutOfCheeseError")
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
    DictsStructMethodArgs m_args;
};


/**
 * @brief A interface using dicts using structs using dicts
 */
class DictsWithStructsInterface : public QObject {
    Q_OBJECT
    QML_ELEMENT
    QML_SINGLETON

    /** @brief Whether the interface is registered and connected */
    Q_PROPERTY(bool connected READ getConnected NOTIFY connectedChanged )

    /**
     * @brief a simple property
     */
    Q_PROPERTY(QMap<$1, $2> dictStructProperty READ getDictStructProperty WRITE setDictStructProperty NOTIFY dictStructPropertyChanged)

public:
    DictsWithStructsInterface(QObject* parent = nullptr);

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
     * @brief Handler for DictsStructMethod D-Bus calls.
     *
     * @param call the D-Bus call object
     */
    void handleDictsStructMethodCalled(QDBusMessage call);


public slots:
    /** @brief Registeres and connects the interface. */
    void connect();

    /** @brief Unregisteres and disconnects the interface. */
    void disconnect();

    /**
     * @brief a simple signal with one argument
     *
     * @param numbers numbers
     */
    void EmitDictStructSignal(
        QMap<$1, $2> numbers
    );

    /**
     * @brief Getter for the DictStructProperty property.
     *
     * @returns the current value of the property
     */
    QMap<$1, $2> getDictStructProperty() const;

    /**
     * @brief Setter for the DictStructProperty property.
     *
     * @param value the new value of the property
     */
    void setDictStructProperty(const QMap<$1, $2> &value );


signals:
    /**
     * @brief Emitted when the connection status changes.
     */
    void connectedChanged();

    /**
     * @brief Emitted when a client calls the DictsStructMethod method.
     *
     * @param reply the reply object containing the call arguments and means to reply
     */
    void dictsStructMethodCalled(DictsStructMethodPendingReply* reply);

    /**
     * @brief Emitted when a client tries to set the DictStructProperty property.
     *
     * @param value the new value of the property
     */
    void propertyDictStructPropertySet(QMap<$1, $2> value);

    /**
     * @brief Emitted when the value of the DictStructProperty property changes.
     */
    void dictStructPropertyChanged();

private:
    void emitPropertiesChangedSignal(const QVariantMap &changedProperties);
    QMap<$1, $2> m_DictStructProperty = {};
};

}