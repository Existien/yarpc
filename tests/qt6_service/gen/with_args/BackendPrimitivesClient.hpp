/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/02.2_primitives.yml
 *   Object: Primitives
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

namespace BackendPrimitivesClientUtils {

/**
 * @brief Pending call object for the Uint8Method method calls.
 */
class Uint8MethodPendingCall : public QObject {
    Q_OBJECT
    QML_UNCREATABLE("")
    QML_ELEMENT
public:
    Uint8MethodPendingCall(QDBusPendingCall pendingCall, QObject *parent);
signals:
    /**
     * @brief Emitted when an Uint8Method call returns.
     *
     * @param the return type
     */
    void finished(const uchar &reply);

    /**
     * @brief Emitted when an error ocurred during an Uint8Method call.
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
 * @brief Pending call object for the BoolMethod method calls.
 */
class BoolMethodPendingCall : public QObject {
    Q_OBJECT
    QML_UNCREATABLE("")
    QML_ELEMENT
public:
    BoolMethodPendingCall(QDBusPendingCall pendingCall, QObject *parent);
signals:
    /**
     * @brief Emitted when an BoolMethod call returns.
     *
     * @param the return type
     */
    void finished(const bool &reply);

    /**
     * @brief Emitted when an error ocurred during an BoolMethod call.
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
 * @brief Pending call object for the Int16Method method calls.
 */
class Int16MethodPendingCall : public QObject {
    Q_OBJECT
    QML_UNCREATABLE("")
    QML_ELEMENT
public:
    Int16MethodPendingCall(QDBusPendingCall pendingCall, QObject *parent);
signals:
    /**
     * @brief Emitted when an Int16Method call returns.
     *
     * @param the return type
     */
    void finished(const short &reply);

    /**
     * @brief Emitted when an error ocurred during an Int16Method call.
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
 * @brief Pending call object for the Uint16Method method calls.
 */
class Uint16MethodPendingCall : public QObject {
    Q_OBJECT
    QML_UNCREATABLE("")
    QML_ELEMENT
public:
    Uint16MethodPendingCall(QDBusPendingCall pendingCall, QObject *parent);
signals:
    /**
     * @brief Emitted when an Uint16Method call returns.
     *
     * @param the return type
     */
    void finished(const ushort &reply);

    /**
     * @brief Emitted when an error ocurred during an Uint16Method call.
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
 * @brief Pending call object for the Int32Method method calls.
 */
class Int32MethodPendingCall : public QObject {
    Q_OBJECT
    QML_UNCREATABLE("")
    QML_ELEMENT
public:
    Int32MethodPendingCall(QDBusPendingCall pendingCall, QObject *parent);
signals:
    /**
     * @brief Emitted when an Int32Method call returns.
     *
     * @param the return type
     */
    void finished(const int &reply);

    /**
     * @brief Emitted when an error ocurred during an Int32Method call.
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
 * @brief Pending call object for the Uint32Method method calls.
 */
class Uint32MethodPendingCall : public QObject {
    Q_OBJECT
    QML_UNCREATABLE("")
    QML_ELEMENT
public:
    Uint32MethodPendingCall(QDBusPendingCall pendingCall, QObject *parent);
signals:
    /**
     * @brief Emitted when an Uint32Method call returns.
     *
     * @param the return type
     */
    void finished(const uint &reply);

    /**
     * @brief Emitted when an error ocurred during an Uint32Method call.
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
 * @brief Pending call object for the Int64Method method calls.
 */
class Int64MethodPendingCall : public QObject {
    Q_OBJECT
    QML_UNCREATABLE("")
    QML_ELEMENT
public:
    Int64MethodPendingCall(QDBusPendingCall pendingCall, QObject *parent);
signals:
    /**
     * @brief Emitted when an Int64Method call returns.
     *
     * @param the return type
     */
    void finished(const qlonglong &reply);

    /**
     * @brief Emitted when an error ocurred during an Int64Method call.
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
 * @brief Pending call object for the Uint64Method method calls.
 */
class Uint64MethodPendingCall : public QObject {
    Q_OBJECT
    QML_UNCREATABLE("")
    QML_ELEMENT
public:
    Uint64MethodPendingCall(QDBusPendingCall pendingCall, QObject *parent);
signals:
    /**
     * @brief Emitted when an Uint64Method call returns.
     *
     * @param the return type
     */
    void finished(const qulonglong &reply);

    /**
     * @brief Emitted when an error ocurred during an Uint64Method call.
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
 * @brief Pending call object for the DoubleMethod method calls.
 */
class DoubleMethodPendingCall : public QObject {
    Q_OBJECT
    QML_UNCREATABLE("")
    QML_ELEMENT
public:
    DoubleMethodPendingCall(QDBusPendingCall pendingCall, QObject *parent);
signals:
    /**
     * @brief Emitted when an DoubleMethod call returns.
     *
     * @param the return type
     */
    void finished(const double &reply);

    /**
     * @brief Emitted when an error ocurred during an DoubleMethod call.
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
 * @brief Pending call object for the StringMethod method calls.
 */
class StringMethodPendingCall : public QObject {
    Q_OBJECT
    QML_UNCREATABLE("")
    QML_ELEMENT
public:
    StringMethodPendingCall(QDBusPendingCall pendingCall, QObject *parent);
signals:
    /**
     * @brief Emitted when an StringMethod call returns.
     *
     * @param the return type
     */
    void finished(const QString &reply);

    /**
     * @brief Emitted when an error ocurred during an StringMethod call.
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
 * D-Bus client for the com.yarpc.backend.primitives D-Bus interface
 */
class BackendPrimitivesClient : public QObject {
    Q_OBJECT
    QML_ELEMENT
    /**
     * @brief Whether the client is connected.
     */
    Q_PROPERTY(bool connected READ getConnected NOTIFY connectedChanged)
public:
    BackendPrimitivesClient(QObject* parent = nullptr);

    /**
     * @brief a method
     *
     * @param value the value
     *
     * @returns Pending call object with finished signal containing the reply.
     */
    BackendPrimitivesClientUtils::Uint8MethodPendingCall* Uint8Method(
        uchar value
    );

    /**
     * @brief a method
     *
     * @param value the value
     *
     * @returns Pending call object with finished signal containing the reply.
     */
    BackendPrimitivesClientUtils::BoolMethodPendingCall* BoolMethod(
        bool value
    );

    /**
     * @brief a method
     *
     * @param value the value
     *
     * @returns Pending call object with finished signal containing the reply.
     */
    BackendPrimitivesClientUtils::Int16MethodPendingCall* Int16Method(
        short value
    );

    /**
     * @brief a method
     *
     * @param value the value
     *
     * @returns Pending call object with finished signal containing the reply.
     */
    BackendPrimitivesClientUtils::Uint16MethodPendingCall* Uint16Method(
        ushort value
    );

    /**
     * @brief a method
     *
     * @param value the value
     *
     * @returns Pending call object with finished signal containing the reply.
     */
    BackendPrimitivesClientUtils::Int32MethodPendingCall* Int32Method(
        int value
    );

    /**
     * @brief a method
     *
     * @param value the value
     *
     * @returns Pending call object with finished signal containing the reply.
     */
    BackendPrimitivesClientUtils::Uint32MethodPendingCall* Uint32Method(
        uint value
    );

    /**
     * @brief a method
     *
     * @param value the value
     *
     * @returns Pending call object with finished signal containing the reply.
     */
    BackendPrimitivesClientUtils::Int64MethodPendingCall* Int64Method(
        qlonglong value
    );

    /**
     * @brief a method
     *
     * @param value the value
     *
     * @returns Pending call object with finished signal containing the reply.
     */
    BackendPrimitivesClientUtils::Uint64MethodPendingCall* Uint64Method(
        qulonglong value
    );

    /**
     * @brief a method
     *
     * @param value the value
     *
     * @returns Pending call object with finished signal containing the reply.
     */
    BackendPrimitivesClientUtils::DoubleMethodPendingCall* DoubleMethod(
        double value
    );

    /**
     * @brief a method
     *
     * @param value the value
     *
     * @returns Pending call object with finished signal containing the reply.
     */
    BackendPrimitivesClientUtils::StringMethodPendingCall* StringMethod(
        QString value
    );

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
     * @brief a method
     *
     * @param value the value
     *
     * @returns Pending call object with finished signal containing the reply.
     */
    BackendPrimitivesClientUtils::Uint8MethodPendingCall* Uint8Method(
        QVariant value
    );

    /**
     * @brief a method
     *
     * @param value the value
     *
     * @returns Pending call object with finished signal containing the reply.
     */
    BackendPrimitivesClientUtils::BoolMethodPendingCall* BoolMethod(
        QVariant value
    );

    /**
     * @brief a method
     *
     * @param value the value
     *
     * @returns Pending call object with finished signal containing the reply.
     */
    BackendPrimitivesClientUtils::Int16MethodPendingCall* Int16Method(
        QVariant value
    );

    /**
     * @brief a method
     *
     * @param value the value
     *
     * @returns Pending call object with finished signal containing the reply.
     */
    BackendPrimitivesClientUtils::Uint16MethodPendingCall* Uint16Method(
        QVariant value
    );

    /**
     * @brief a method
     *
     * @param value the value
     *
     * @returns Pending call object with finished signal containing the reply.
     */
    BackendPrimitivesClientUtils::Int32MethodPendingCall* Int32Method(
        QVariant value
    );

    /**
     * @brief a method
     *
     * @param value the value
     *
     * @returns Pending call object with finished signal containing the reply.
     */
    BackendPrimitivesClientUtils::Uint32MethodPendingCall* Uint32Method(
        QVariant value
    );

    /**
     * @brief a method
     *
     * @param value the value
     *
     * @returns Pending call object with finished signal containing the reply.
     */
    BackendPrimitivesClientUtils::Int64MethodPendingCall* Int64Method(
        QVariant value
    );

    /**
     * @brief a method
     *
     * @param value the value
     *
     * @returns Pending call object with finished signal containing the reply.
     */
    BackendPrimitivesClientUtils::Uint64MethodPendingCall* Uint64Method(
        QVariant value
    );

    /**
     * @brief a method
     *
     * @param value the value
     *
     * @returns Pending call object with finished signal containing the reply.
     */
    BackendPrimitivesClientUtils::DoubleMethodPendingCall* DoubleMethod(
        QVariant value
    );

    /**
     * @brief a method
     *
     * @param value the value
     *
     * @returns Pending call object with finished signal containing the reply.
     */
    BackendPrimitivesClientUtils::StringMethodPendingCall* StringMethod(
        QVariant value
    );

signals:
    /**
     * @brief Emitted when the connected property changes.
     */
    void connectedChanged();

    /**
     * @brief a signal
     *
     * @param value the value
     */
    void uint8SignalReceived(
        QVariant value
    );

    /**
     * @brief a signal
     *
     * @param value the value
     */
    void boolSignalReceived(
        QVariant value
    );

    /**
     * @brief a signal
     *
     * @param value the value
     */
    void int16SignalReceived(
        QVariant value
    );

    /**
     * @brief a signal
     *
     * @param value the value
     */
    void uint16SignalReceived(
        QVariant value
    );

    /**
     * @brief a signal
     *
     * @param value the value
     */
    void int32SignalReceived(
        QVariant value
    );

    /**
     * @brief a signal
     *
     * @param value the value
     */
    void uint32SignalReceived(
        QVariant value
    );

    /**
     * @brief a signal
     *
     * @param value the value
     */
    void int64SignalReceived(
        QVariant value
    );

    /**
     * @brief a signal
     *
     * @param value the value
     */
    void uint64SignalReceived(
        QVariant value
    );

    /**
     * @brief a signal
     *
     * @param value the value
     */
    void doubleSignalReceived(
        QVariant value
    );

    /**
     * @brief a signal
     *
     * @param value the value
     */
    void stringSignalReceived(
        QVariant value
    );

private slots:
    void connectedHandler(const QString& service);
    void disconnectedHandler(const QString& service);
    void propertiesChangedHandler(QString interface, QVariantMap changes, QStringList);
    void Uint8SignalDBusHandler(QDBusMessage content);
    void BoolSignalDBusHandler(QDBusMessage content);
    void Int16SignalDBusHandler(QDBusMessage content);
    void Uint16SignalDBusHandler(QDBusMessage content);
    void Int32SignalDBusHandler(QDBusMessage content);
    void Uint32SignalDBusHandler(QDBusMessage content);
    void Int64SignalDBusHandler(QDBusMessage content);
    void Uint64SignalDBusHandler(QDBusMessage content);
    void DoubleSignalDBusHandler(QDBusMessage content);
    void StringSignalDBusHandler(QDBusMessage content);
private:
    bool m_connected = false;
    QDBusServiceWatcher m_watcher;
};

}