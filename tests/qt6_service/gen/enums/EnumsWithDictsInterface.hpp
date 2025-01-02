/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/06.3_enums_with_dicts.yml
 *   Object: EnumsWithDicts
 *   Template: qt6/service_header.j2
 */
#pragma once
#include <QObject>
#include <qqmlintegration.h>
#include <QDBusMessage>
#include <QVariant>
#include "DBusError.hpp"
#include "EnumStruct.hpp"
#include "types.hpp"
namespace gen::enums {

/**
 * @brief The arguments passed during a EnumMethod call.
 */
class EnumMethodArgs {
    Q_GADGET
    /**
     * @brief a color
     */
    Q_PROPERTY(QMap<, > color MEMBER color)
public:
    QMap<, > color;
};

/**
 * @brief A pending reply to a EnumMethod call.
 *
 * Use the sendReply or sendError methods to send the pending reply.
 */
class EnumMethodPendingReply : public QObject {
    Q_OBJECT
    QML_UNCREATABLE("")
    QML_ELEMENT
public:
    EnumMethodPendingReply(QDBusMessage call, QObject *parent);

    /**
     * @brief Send a reply to the pending call.
     *
     * @param reply the return value of the call
     */
    void sendReply(
        const QMap<, > &reply
    );
public slots:
    /**
     * @brief Returns the arguments passed during a EnumMethod call.
     *
     * @returns the arguments of the call
     */
    EnumMethodArgs args();

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
     *   (needs to be in the form of a D-Bus URI, e.g. "com.yarpc.testservice.enumsWithDicts.OutOfCheeseError")
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
    EnumMethodArgs m_args;
};


/**
 * @brief A interface using enums in dictionaries
 */
class EnumsWithDictsInterface : public QObject {
    Q_OBJECT
    QML_ELEMENT
    QML_SINGLETON

    /** @brief Whether the interface is registered and connected */
    Q_PROPERTY(bool connected READ getConnected NOTIFY connectedChanged )

    /**
     * @brief a property
     */
    Q_PROPERTY(QVariant enumProperty READ getVariantEnumProperty WRITE setVariantEnumProperty NOTIFY enumPropertyChanged)

public:
    EnumsWithDictsInterface(QObject* parent = nullptr);

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
     * @brief Handler for EnumMethod D-Bus calls.
     *
     * @param call the D-Bus call object
     */
    void handleEnumMethodCalled(QDBusMessage call);

    /**
     * @brief Getter for the EnumProperty property.
     *
     * @returns the current value of the property
     */
    QMap<, > getEnumProperty() const;

    /**
     * @brief Setter for the EnumProperty property.
     *
     * @param value the new value of the property
     */
    void setEnumProperty(const QMap<, > &value );


    /**
     * @brief a simple signal with one argument
     *
     * @param color a color
     */
    void EmitEnumSignal(
        QMap<, > color
    );


public slots:
    /** @brief Registeres and connects the interface. */
    void connect();

    /** @brief Unregisteres and disconnects the interface. */
    void disconnect();

    /**
     * @brief a simple signal with one argument
     *
     * @param color a color
     */
    void EmitEnumSignal(
        QVariant color
    );


private:

    /**
     * @brief Getter for the EnumProperty property as variant.
     *
     * @returns the current value of the property as variant
     */
    QVariant getVariantEnumProperty() const;

    /**
     * @brief Setter for the EnumProperty property as variant.
     *
     * @param value the new value of the property wrapped in a variant
     */
    void setVariantEnumProperty(QVariant value );


signals:
    /**
     * @brief Emitted when the connection status changes.
     */
    void connectedChanged();

    /**
     * @brief Emitted when a client calls the EnumMethod method.
     *
     * @param reply the reply object containing the call arguments and means to reply
     */
    void enumMethodCalled(EnumMethodPendingReply* reply);

    /**
     * @brief Emitted when a client tries to set the EnumProperty property.
     *
     * @param value the new value of the property
     */
    void propertyEnumPropertySet(QMap<, > value);

    /**
     * @brief Emitted when the value of the EnumProperty property changes.
     */
    void enumPropertyChanged();

private:
    void emitPropertiesChangedSignal(const QVariantMap &changedProperties);
    QMap<, > m_EnumProperty = {};
};

}