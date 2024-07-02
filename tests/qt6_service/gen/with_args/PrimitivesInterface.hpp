/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/02.2_primitives.yml
 *   Object: Primitives
 *   Template: qt6/service_header.j2
 */
#pragma once
#include <QObject>
#include <qqmlintegration.h>
#include <QDBusMessage>
#include <QVariant>
#include "DBusError.hpp"
namespace gen::with_args {

/**
 * @brief The arguments passed during a Uint8Method call.
 */
class Uint8MethodArgs {
    Q_GADGET
    /**
     * @brief the value
     */
    Q_PROPERTY(uchar value MEMBER value)
public:
    uchar value;
};

/**
 * @brief A pending reply to a Uint8Method call.
 *
 * Use the sendReply or sendError methods to send the pending reply.
 */
class Uint8MethodPendingReply : public QObject {
    Q_OBJECT
    QML_UNCREATABLE("")
    QML_ELEMENT
public:
    Uint8MethodPendingReply(QDBusMessage call, QObject *parent);

    /**
     * @brief Send a reply to the pending call.
     *
     * @param reply the return value of the call
     */
    void sendReply(
        const uchar &reply
    );
public slots:
    /**
     * @brief Returns the arguments passed during a Uint8Method call.
     *
     * @returns the arguments of the call
     */
    Uint8MethodArgs args();

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
     *   (needs to be in the form of a D-Bus URI, e.g. "com.yarpc.testservice.primitives.OutOfCheeseError")
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
    Uint8MethodArgs m_args;
};

/**
 * @brief The arguments passed during a BoolMethod call.
 */
class BoolMethodArgs {
    Q_GADGET
    /**
     * @brief the value
     */
    Q_PROPERTY(bool value MEMBER value)
public:
    bool value;
};

/**
 * @brief A pending reply to a BoolMethod call.
 *
 * Use the sendReply or sendError methods to send the pending reply.
 */
class BoolMethodPendingReply : public QObject {
    Q_OBJECT
    QML_UNCREATABLE("")
    QML_ELEMENT
public:
    BoolMethodPendingReply(QDBusMessage call, QObject *parent);

    /**
     * @brief Send a reply to the pending call.
     *
     * @param reply the return value of the call
     */
    void sendReply(
        const bool &reply
    );
public slots:
    /**
     * @brief Returns the arguments passed during a BoolMethod call.
     *
     * @returns the arguments of the call
     */
    BoolMethodArgs args();

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
     *   (needs to be in the form of a D-Bus URI, e.g. "com.yarpc.testservice.primitives.OutOfCheeseError")
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
    BoolMethodArgs m_args;
};

/**
 * @brief The arguments passed during a Int16Method call.
 */
class Int16MethodArgs {
    Q_GADGET
    /**
     * @brief the value
     */
    Q_PROPERTY(short value MEMBER value)
public:
    short value;
};

/**
 * @brief A pending reply to a Int16Method call.
 *
 * Use the sendReply or sendError methods to send the pending reply.
 */
class Int16MethodPendingReply : public QObject {
    Q_OBJECT
    QML_UNCREATABLE("")
    QML_ELEMENT
public:
    Int16MethodPendingReply(QDBusMessage call, QObject *parent);

    /**
     * @brief Send a reply to the pending call.
     *
     * @param reply the return value of the call
     */
    void sendReply(
        const short &reply
    );
public slots:
    /**
     * @brief Returns the arguments passed during a Int16Method call.
     *
     * @returns the arguments of the call
     */
    Int16MethodArgs args();

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
     *   (needs to be in the form of a D-Bus URI, e.g. "com.yarpc.testservice.primitives.OutOfCheeseError")
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
    Int16MethodArgs m_args;
};

/**
 * @brief The arguments passed during a Uint16Method call.
 */
class Uint16MethodArgs {
    Q_GADGET
    /**
     * @brief the value
     */
    Q_PROPERTY(ushort value MEMBER value)
public:
    ushort value;
};

/**
 * @brief A pending reply to a Uint16Method call.
 *
 * Use the sendReply or sendError methods to send the pending reply.
 */
class Uint16MethodPendingReply : public QObject {
    Q_OBJECT
    QML_UNCREATABLE("")
    QML_ELEMENT
public:
    Uint16MethodPendingReply(QDBusMessage call, QObject *parent);

    /**
     * @brief Send a reply to the pending call.
     *
     * @param reply the return value of the call
     */
    void sendReply(
        const ushort &reply
    );
public slots:
    /**
     * @brief Returns the arguments passed during a Uint16Method call.
     *
     * @returns the arguments of the call
     */
    Uint16MethodArgs args();

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
     *   (needs to be in the form of a D-Bus URI, e.g. "com.yarpc.testservice.primitives.OutOfCheeseError")
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
    Uint16MethodArgs m_args;
};

/**
 * @brief The arguments passed during a Int32Method call.
 */
class Int32MethodArgs {
    Q_GADGET
    /**
     * @brief the value
     */
    Q_PROPERTY(int value MEMBER value)
public:
    int value;
};

/**
 * @brief A pending reply to a Int32Method call.
 *
 * Use the sendReply or sendError methods to send the pending reply.
 */
class Int32MethodPendingReply : public QObject {
    Q_OBJECT
    QML_UNCREATABLE("")
    QML_ELEMENT
public:
    Int32MethodPendingReply(QDBusMessage call, QObject *parent);

    /**
     * @brief Send a reply to the pending call.
     *
     * @param reply the return value of the call
     */
    void sendReply(
        const int &reply
    );
public slots:
    /**
     * @brief Returns the arguments passed during a Int32Method call.
     *
     * @returns the arguments of the call
     */
    Int32MethodArgs args();

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
     *   (needs to be in the form of a D-Bus URI, e.g. "com.yarpc.testservice.primitives.OutOfCheeseError")
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
    Int32MethodArgs m_args;
};

/**
 * @brief The arguments passed during a Uint32Method call.
 */
class Uint32MethodArgs {
    Q_GADGET
    /**
     * @brief the value
     */
    Q_PROPERTY(uint value MEMBER value)
public:
    uint value;
};

/**
 * @brief A pending reply to a Uint32Method call.
 *
 * Use the sendReply or sendError methods to send the pending reply.
 */
class Uint32MethodPendingReply : public QObject {
    Q_OBJECT
    QML_UNCREATABLE("")
    QML_ELEMENT
public:
    Uint32MethodPendingReply(QDBusMessage call, QObject *parent);

    /**
     * @brief Send a reply to the pending call.
     *
     * @param reply the return value of the call
     */
    void sendReply(
        const uint &reply
    );
public slots:
    /**
     * @brief Returns the arguments passed during a Uint32Method call.
     *
     * @returns the arguments of the call
     */
    Uint32MethodArgs args();

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
     *   (needs to be in the form of a D-Bus URI, e.g. "com.yarpc.testservice.primitives.OutOfCheeseError")
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
    Uint32MethodArgs m_args;
};

/**
 * @brief The arguments passed during a Int64Method call.
 */
class Int64MethodArgs {
    Q_GADGET
    /**
     * @brief the value
     */
    Q_PROPERTY(qlonglong value MEMBER value)
public:
    qlonglong value;
};

/**
 * @brief A pending reply to a Int64Method call.
 *
 * Use the sendReply or sendError methods to send the pending reply.
 */
class Int64MethodPendingReply : public QObject {
    Q_OBJECT
    QML_UNCREATABLE("")
    QML_ELEMENT
public:
    Int64MethodPendingReply(QDBusMessage call, QObject *parent);

    /**
     * @brief Send a reply to the pending call.
     *
     * @param reply the return value of the call
     */
    void sendReply(
        const qlonglong &reply
    );
public slots:
    /**
     * @brief Returns the arguments passed during a Int64Method call.
     *
     * @returns the arguments of the call
     */
    Int64MethodArgs args();

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
     *   (needs to be in the form of a D-Bus URI, e.g. "com.yarpc.testservice.primitives.OutOfCheeseError")
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
    Int64MethodArgs m_args;
};

/**
 * @brief The arguments passed during a Uint64Method call.
 */
class Uint64MethodArgs {
    Q_GADGET
    /**
     * @brief the value
     */
    Q_PROPERTY(qulonglong value MEMBER value)
public:
    qulonglong value;
};

/**
 * @brief A pending reply to a Uint64Method call.
 *
 * Use the sendReply or sendError methods to send the pending reply.
 */
class Uint64MethodPendingReply : public QObject {
    Q_OBJECT
    QML_UNCREATABLE("")
    QML_ELEMENT
public:
    Uint64MethodPendingReply(QDBusMessage call, QObject *parent);

    /**
     * @brief Send a reply to the pending call.
     *
     * @param reply the return value of the call
     */
    void sendReply(
        const qulonglong &reply
    );
public slots:
    /**
     * @brief Returns the arguments passed during a Uint64Method call.
     *
     * @returns the arguments of the call
     */
    Uint64MethodArgs args();

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
     *   (needs to be in the form of a D-Bus URI, e.g. "com.yarpc.testservice.primitives.OutOfCheeseError")
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
    Uint64MethodArgs m_args;
};

/**
 * @brief The arguments passed during a DoubleMethod call.
 */
class DoubleMethodArgs {
    Q_GADGET
    /**
     * @brief the value
     */
    Q_PROPERTY(double value MEMBER value)
public:
    double value;
};

/**
 * @brief A pending reply to a DoubleMethod call.
 *
 * Use the sendReply or sendError methods to send the pending reply.
 */
class DoubleMethodPendingReply : public QObject {
    Q_OBJECT
    QML_UNCREATABLE("")
    QML_ELEMENT
public:
    DoubleMethodPendingReply(QDBusMessage call, QObject *parent);

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
     * @brief Returns the arguments passed during a DoubleMethod call.
     *
     * @returns the arguments of the call
     */
    DoubleMethodArgs args();

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
     *   (needs to be in the form of a D-Bus URI, e.g. "com.yarpc.testservice.primitives.OutOfCheeseError")
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
    DoubleMethodArgs m_args;
};

/**
 * @brief The arguments passed during a StringMethod call.
 */
class StringMethodArgs {
    Q_GADGET
    /**
     * @brief the value
     */
    Q_PROPERTY(QString value MEMBER value)
public:
    QString value;
};

/**
 * @brief A pending reply to a StringMethod call.
 *
 * Use the sendReply or sendError methods to send the pending reply.
 */
class StringMethodPendingReply : public QObject {
    Q_OBJECT
    QML_UNCREATABLE("")
    QML_ELEMENT
public:
    StringMethodPendingReply(QDBusMessage call, QObject *parent);

    /**
     * @brief Send a reply to the pending call.
     *
     * @param reply the return value of the call
     */
    void sendReply(
        const QString &reply
    );
public slots:
    /**
     * @brief Returns the arguments passed during a StringMethod call.
     *
     * @returns the arguments of the call
     */
    StringMethodArgs args();

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
     *   (needs to be in the form of a D-Bus URI, e.g. "com.yarpc.testservice.primitives.OutOfCheeseError")
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
    StringMethodArgs m_args;
};


/**
 * @brief A interface using all builtin primitive types
 */
class PrimitivesInterface : public QObject {
    Q_OBJECT
    QML_ELEMENT
    QML_SINGLETON

    /** @brief Whether the interface is registered and connected */
    Q_PROPERTY(bool connected READ getConnected NOTIFY connectedChanged )

public:
    PrimitivesInterface(QObject* parent = nullptr);

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
     * @brief Handler for Uint8Method D-Bus calls.
     *
     * @param call the D-Bus call object
     */
    void handleUint8MethodCalled(QDBusMessage call);


    /**
     * @brief Handler for BoolMethod D-Bus calls.
     *
     * @param call the D-Bus call object
     */
    void handleBoolMethodCalled(QDBusMessage call);


    /**
     * @brief Handler for Int16Method D-Bus calls.
     *
     * @param call the D-Bus call object
     */
    void handleInt16MethodCalled(QDBusMessage call);


    /**
     * @brief Handler for Uint16Method D-Bus calls.
     *
     * @param call the D-Bus call object
     */
    void handleUint16MethodCalled(QDBusMessage call);


    /**
     * @brief Handler for Int32Method D-Bus calls.
     *
     * @param call the D-Bus call object
     */
    void handleInt32MethodCalled(QDBusMessage call);


    /**
     * @brief Handler for Uint32Method D-Bus calls.
     *
     * @param call the D-Bus call object
     */
    void handleUint32MethodCalled(QDBusMessage call);


    /**
     * @brief Handler for Int64Method D-Bus calls.
     *
     * @param call the D-Bus call object
     */
    void handleInt64MethodCalled(QDBusMessage call);


    /**
     * @brief Handler for Uint64Method D-Bus calls.
     *
     * @param call the D-Bus call object
     */
    void handleUint64MethodCalled(QDBusMessage call);


    /**
     * @brief Handler for DoubleMethod D-Bus calls.
     *
     * @param call the D-Bus call object
     */
    void handleDoubleMethodCalled(QDBusMessage call);


    /**
     * @brief Handler for StringMethod D-Bus calls.
     *
     * @param call the D-Bus call object
     */
    void handleStringMethodCalled(QDBusMessage call);



    /**
     * @brief a signal
     *
     * @param value the value
     */
    void EmitUint8Signal(
        uchar value
    );

    /**
     * @brief a signal
     *
     * @param value the value
     */
    void EmitBoolSignal(
        bool value
    );

    /**
     * @brief a signal
     *
     * @param value the value
     */
    void EmitInt16Signal(
        short value
    );

    /**
     * @brief a signal
     *
     * @param value the value
     */
    void EmitUint16Signal(
        ushort value
    );

    /**
     * @brief a signal
     *
     * @param value the value
     */
    void EmitInt32Signal(
        int value
    );

    /**
     * @brief a signal
     *
     * @param value the value
     */
    void EmitUint32Signal(
        uint value
    );

    /**
     * @brief a signal
     *
     * @param value the value
     */
    void EmitInt64Signal(
        qlonglong value
    );

    /**
     * @brief a signal
     *
     * @param value the value
     */
    void EmitUint64Signal(
        qulonglong value
    );

    /**
     * @brief a signal
     *
     * @param value the value
     */
    void EmitDoubleSignal(
        double value
    );

    /**
     * @brief a signal
     *
     * @param value the value
     */
    void EmitStringSignal(
        QString value
    );


public slots:
    /** @brief Registeres and connects the interface. */
    void connect();

    /** @brief Unregisteres and disconnects the interface. */
    void disconnect();

    /**
     * @brief a signal
     *
     * @param value the value
     */
    void EmitUint8Signal(
        QVariant value
    );

    /**
     * @brief a signal
     *
     * @param value the value
     */
    void EmitBoolSignal(
        QVariant value
    );

    /**
     * @brief a signal
     *
     * @param value the value
     */
    void EmitInt16Signal(
        QVariant value
    );

    /**
     * @brief a signal
     *
     * @param value the value
     */
    void EmitUint16Signal(
        QVariant value
    );

    /**
     * @brief a signal
     *
     * @param value the value
     */
    void EmitInt32Signal(
        QVariant value
    );

    /**
     * @brief a signal
     *
     * @param value the value
     */
    void EmitUint32Signal(
        QVariant value
    );

    /**
     * @brief a signal
     *
     * @param value the value
     */
    void EmitInt64Signal(
        QVariant value
    );

    /**
     * @brief a signal
     *
     * @param value the value
     */
    void EmitUint64Signal(
        QVariant value
    );

    /**
     * @brief a signal
     *
     * @param value the value
     */
    void EmitDoubleSignal(
        QVariant value
    );

    /**
     * @brief a signal
     *
     * @param value the value
     */
    void EmitStringSignal(
        QVariant value
    );


private:


signals:
    /**
     * @brief Emitted when the connection status changes.
     */
    void connectedChanged();

    /**
     * @brief Emitted when a client calls the Uint8Method method.
     *
     * @param reply the reply object containing the call arguments and means to reply
     */
    void uint8MethodCalled(Uint8MethodPendingReply* reply);

    /**
     * @brief Emitted when a client calls the BoolMethod method.
     *
     * @param reply the reply object containing the call arguments and means to reply
     */
    void boolMethodCalled(BoolMethodPendingReply* reply);

    /**
     * @brief Emitted when a client calls the Int16Method method.
     *
     * @param reply the reply object containing the call arguments and means to reply
     */
    void int16MethodCalled(Int16MethodPendingReply* reply);

    /**
     * @brief Emitted when a client calls the Uint16Method method.
     *
     * @param reply the reply object containing the call arguments and means to reply
     */
    void uint16MethodCalled(Uint16MethodPendingReply* reply);

    /**
     * @brief Emitted when a client calls the Int32Method method.
     *
     * @param reply the reply object containing the call arguments and means to reply
     */
    void int32MethodCalled(Int32MethodPendingReply* reply);

    /**
     * @brief Emitted when a client calls the Uint32Method method.
     *
     * @param reply the reply object containing the call arguments and means to reply
     */
    void uint32MethodCalled(Uint32MethodPendingReply* reply);

    /**
     * @brief Emitted when a client calls the Int64Method method.
     *
     * @param reply the reply object containing the call arguments and means to reply
     */
    void int64MethodCalled(Int64MethodPendingReply* reply);

    /**
     * @brief Emitted when a client calls the Uint64Method method.
     *
     * @param reply the reply object containing the call arguments and means to reply
     */
    void uint64MethodCalled(Uint64MethodPendingReply* reply);

    /**
     * @brief Emitted when a client calls the DoubleMethod method.
     *
     * @param reply the reply object containing the call arguments and means to reply
     */
    void doubleMethodCalled(DoubleMethodPendingReply* reply);

    /**
     * @brief Emitted when a client calls the StringMethod method.
     *
     * @param reply the reply object containing the call arguments and means to reply
     */
    void stringMethodCalled(StringMethodPendingReply* reply);


private:
    void emitPropertiesChangedSignal(const QVariantMap &changedProperties);
};

}