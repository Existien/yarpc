/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/04.2_arrays_with_structs.yml
 *   Object: ArraysWithStructs
 *   Template: qt6/service_header.j2
 */
#pragma once
#include <QObject>
#include <qqmlintegration.h>
#include <QDBusMessage>
#include <QVariant>
#include "DBusError.hpp"
#include "StructArray.hpp"
#include "SimonsArray.hpp"
#include "types.hpp"
namespace gen::arrays {

/**
 * @brief The arguments passed during a ArrayStructMethod call.
 */
class ArrayStructMethodArgs {
    Q_GADGET
    /**
     * @brief Some numbers
     */
    Q_PROPERTY(QList<StructArray> numbers MEMBER numbers)
public:
    QList<StructArray> numbers;
};

/**
 * @brief A pending reply to a ArrayStructMethod call.
 *
 * Use the sendReply or sendError methods to send the pending reply.
 */
class ArrayStructMethodPendingReply : public QObject {
    Q_OBJECT
    QML_UNCREATABLE("")
    QML_ELEMENT
public:
    ArrayStructMethodPendingReply(QDBusMessage call, QObject *parent);

    /**
     * @brief Send a reply to the pending call.
     *
     * @param reply the return value of the call
     */
    void sendReply(
        const QList<SimonsArray> &reply
    );
public slots:
    /**
     * @brief Returns the arguments passed during a ArrayStructMethod call.
     *
     * @returns the arguments of the call
     */
    ArrayStructMethodArgs args();

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
     *   (needs to be in the form of a D-Bus URI, e.g. "com.yarpc.testservice.arraysWithStructs.OutOfCheeseError")
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
    ArrayStructMethodArgs m_args;
};


/**
 * @brief A interface using arrays using structs using arrays
 */
class ArraysWithStructsInterface : public QObject {
    Q_OBJECT
    QML_ELEMENT
    QML_SINGLETON

    /** @brief Whether the interface is registered and connected */
    Q_PROPERTY(bool connected READ getConnected NOTIFY connectedChanged )

    /**
     * @brief a simple property
     */
    Q_PROPERTY(QVariant arrayStructProperty READ getVariantArrayStructProperty WRITE setVariantArrayStructProperty NOTIFY arrayStructPropertyChanged)

public:
    ArraysWithStructsInterface(QObject* parent = nullptr);

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
     * @brief Handler for ArrayStructMethod D-Bus calls.
     *
     * @param call the D-Bus call object
     */
    void handleArrayStructMethodCalled(QDBusMessage call);

    /**
     * @brief Getter for the ArrayStructProperty property.
     *
     * @returns the current value of the property
     */
    QList<StructArray> getArrayStructProperty() const;

    /**
     * @brief Setter for the ArrayStructProperty property.
     *
     * @param value the new value of the property
     */
    void setArrayStructProperty(const QList<StructArray> &value );


    /**
     * @brief a simple signal with one argument
     *
     * @param numbers numbers
     */
    void EmitArrayStructSignal(
        QList<StructArray> numbers
    );


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
    void EmitArrayStructSignal(
        QVariant numbers
    );


private:

    /**
     * @brief Getter for the ArrayStructProperty property as variant.
     *
     * @returns the current value of the property as variant
     */
    QVariant getVariantArrayStructProperty() const;

    /**
     * @brief Setter for the ArrayStructProperty property as variant.
     *
     * @param value the new value of the property wrapped in a variant
     */
    void setVariantArrayStructProperty(QVariant value );


signals:
    /**
     * @brief Emitted when the connection status changes.
     */
    void connectedChanged();

    /**
     * @brief Emitted when a client calls the ArrayStructMethod method.
     *
     * @param reply the reply object containing the call arguments and means to reply
     */
    void arrayStructMethodCalled(ArrayStructMethodPendingReply* reply);

    /**
     * @brief Emitted when a client tries to set the ArrayStructProperty property.
     *
     * @param value the new value of the property
     */
    void propertyArrayStructPropertySet(QList<StructArray> value);

    /**
     * @brief Emitted when the value of the ArrayStructProperty property changes.
     */
    void arrayStructPropertyChanged();

private:
    void emitPropertiesChangedSignal(const QVariantMap &changedProperties);
    QList<StructArray> m_ArrayStructProperty = {};
};

}