/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/05.4_dictionaries_keys.yml
 *   Object: DictKeys
 *   Template: qt6/client_source.j2
 */
#include "BackendDictKeysClient.hpp"
#include "types.hpp"
#include <QDBusConnection>
#include <QDBusInterface>
#include <QDBusReply>
#include <QDBusPendingCall>
#include <QDBusPendingReply>


using namespace gen::dicts;

BackendDictKeysClient::BackendDictKeysClient(QObject* parent)
 : QObject(parent),
   m_watcher(QDBusServiceWatcher(
    "com.yarpc.backend",
    QDBusConnection::sessionBus(),
    QDBusServiceWatcher::WatchForRegistration | QDBusServiceWatcher::WatchForUnregistration,
    parent
   ))
{
    registerMetaTypes();
    QDBusInterface iface(
        "com.yarpc.backend",
        "/com/yarpc/backend/dicts",
        "com.yarpc.backend.dictKeys",
        QDBusConnection::sessionBus()
    );
    m_connected = iface.isValid();

    connect(
        &m_watcher, &QDBusServiceWatcher::serviceRegistered,
        this, &BackendDictKeysClient::connectedHandler
    );
    connect(
        &m_watcher, &QDBusServiceWatcher::serviceUnregistered,
        this, &BackendDictKeysClient::disconnectedHandler
    );

    QDBusConnection::sessionBus().connect(
        "com.yarpc.backend",
        "/com/yarpc/backend/dicts",
        "org.freedesktop.DBus.Properties",
        "PropertiesChanged",
        this,
        SLOT(propertiesChangedHandler(QString, QVariantMap, QStringList))
    );
    QDBusConnection::sessionBus().connect(
        "com.yarpc.backend",
        "/com/yarpc/backend/dicts",
        "com.yarpc.backend.dictKeys",
        "Uint8Signal",
        this,
        SLOT(Uint8SignalDBusHandler(QDBusMessage))
    );
    QDBusConnection::sessionBus().connect(
        "com.yarpc.backend",
        "/com/yarpc/backend/dicts",
        "com.yarpc.backend.dictKeys",
        "BoolSignal",
        this,
        SLOT(BoolSignalDBusHandler(QDBusMessage))
    );
    QDBusConnection::sessionBus().connect(
        "com.yarpc.backend",
        "/com/yarpc/backend/dicts",
        "com.yarpc.backend.dictKeys",
        "Int16Signal",
        this,
        SLOT(Int16SignalDBusHandler(QDBusMessage))
    );
    QDBusConnection::sessionBus().connect(
        "com.yarpc.backend",
        "/com/yarpc/backend/dicts",
        "com.yarpc.backend.dictKeys",
        "Uint16Signal",
        this,
        SLOT(Uint16SignalDBusHandler(QDBusMessage))
    );
    QDBusConnection::sessionBus().connect(
        "com.yarpc.backend",
        "/com/yarpc/backend/dicts",
        "com.yarpc.backend.dictKeys",
        "Int32Signal",
        this,
        SLOT(Int32SignalDBusHandler(QDBusMessage))
    );
    QDBusConnection::sessionBus().connect(
        "com.yarpc.backend",
        "/com/yarpc/backend/dicts",
        "com.yarpc.backend.dictKeys",
        "Uint32Signal",
        this,
        SLOT(Uint32SignalDBusHandler(QDBusMessage))
    );
    QDBusConnection::sessionBus().connect(
        "com.yarpc.backend",
        "/com/yarpc/backend/dicts",
        "com.yarpc.backend.dictKeys",
        "Int64Signal",
        this,
        SLOT(Int64SignalDBusHandler(QDBusMessage))
    );
    QDBusConnection::sessionBus().connect(
        "com.yarpc.backend",
        "/com/yarpc/backend/dicts",
        "com.yarpc.backend.dictKeys",
        "Uint64Signal",
        this,
        SLOT(Uint64SignalDBusHandler(QDBusMessage))
    );
    QDBusConnection::sessionBus().connect(
        "com.yarpc.backend",
        "/com/yarpc/backend/dicts",
        "com.yarpc.backend.dictKeys",
        "DoubleSignal",
        this,
        SLOT(DoubleSignalDBusHandler(QDBusMessage))
    );
    QDBusConnection::sessionBus().connect(
        "com.yarpc.backend",
        "/com/yarpc/backend/dicts",
        "com.yarpc.backend.dictKeys",
        "StringSignal",
        this,
        SLOT(StringSignalDBusHandler(QDBusMessage))
    );

}

bool BackendDictKeysClient::getConnected() const {
    return m_connected;
}

QVariantMap BackendDictKeysClient::getAllProperties() const {
    QDBusInterface iface(
        "com.yarpc.backend",
        "/com/yarpc/backend/dicts",
        "org.freedesktop.DBus.Properties",
        QDBusConnection::sessionBus()
    );
    QDBusReply<QVariantMap> reply = iface.call(
        "GetAll",
        "com.yarpc.backend.dictKeys"
    );
    if (!reply.isValid()) {
        return QVariantMap();
    } else {
        return reply.value();
    }
}

void BackendDictKeysClient::connectedHandler(const QString& service) {
    m_connected = true;
    emit connectedChanged();
}

void BackendDictKeysClient::disconnectedHandler(const QString& service) {
    m_connected = false;
    emit connectedChanged();
}

void BackendDictKeysClient::propertiesChangedHandler(QString iface, QVariantMap changes, QStringList) {
    if (iface != "com.yarpc.backend.dictKeys") {
        return;
    }
}


void BackendDictKeysClient::Uint8SignalDBusHandler(QDBusMessage content) {
    QMap<uchar, QString> arg_0;
    content.arguments()[0].value<QDBusArgument>() >> arg_0;
    emit uint8SignalReceived(
        QVariant::fromValue(arg_0)
    );
}

void BackendDictKeysClient::BoolSignalDBusHandler(QDBusMessage content) {
    QMap<bool, QString> arg_0;
    content.arguments()[0].value<QDBusArgument>() >> arg_0;
    emit boolSignalReceived(
        QVariant::fromValue(arg_0)
    );
}

void BackendDictKeysClient::Int16SignalDBusHandler(QDBusMessage content) {
    QMap<short, QString> arg_0;
    content.arguments()[0].value<QDBusArgument>() >> arg_0;
    emit int16SignalReceived(
        QVariant::fromValue(arg_0)
    );
}

void BackendDictKeysClient::Uint16SignalDBusHandler(QDBusMessage content) {
    QMap<ushort, QString> arg_0;
    content.arguments()[0].value<QDBusArgument>() >> arg_0;
    emit uint16SignalReceived(
        QVariant::fromValue(arg_0)
    );
}

void BackendDictKeysClient::Int32SignalDBusHandler(QDBusMessage content) {
    QMap<int, QString> arg_0;
    content.arguments()[0].value<QDBusArgument>() >> arg_0;
    emit int32SignalReceived(
        QVariant::fromValue(arg_0)
    );
}

void BackendDictKeysClient::Uint32SignalDBusHandler(QDBusMessage content) {
    QMap<uint, QString> arg_0;
    content.arguments()[0].value<QDBusArgument>() >> arg_0;
    emit uint32SignalReceived(
        QVariant::fromValue(arg_0)
    );
}

void BackendDictKeysClient::Int64SignalDBusHandler(QDBusMessage content) {
    QMap<qlonglong, QString> arg_0;
    content.arguments()[0].value<QDBusArgument>() >> arg_0;
    emit int64SignalReceived(
        QVariant::fromValue(arg_0)
    );
}

void BackendDictKeysClient::Uint64SignalDBusHandler(QDBusMessage content) {
    QMap<qulonglong, QString> arg_0;
    content.arguments()[0].value<QDBusArgument>() >> arg_0;
    emit uint64SignalReceived(
        QVariant::fromValue(arg_0)
    );
}

void BackendDictKeysClient::DoubleSignalDBusHandler(QDBusMessage content) {
    QMap<double, QString> arg_0;
    content.arguments()[0].value<QDBusArgument>() >> arg_0;
    emit doubleSignalReceived(
        QVariant::fromValue(arg_0)
    );
}

void BackendDictKeysClient::StringSignalDBusHandler(QDBusMessage content) {
    QMap<QString, QString> arg_0;
    content.arguments()[0].value<QDBusArgument>() >> arg_0;
    emit stringSignalReceived(
        QVariant::fromValue(arg_0)
    );
}
Uint8MethodPendingCall* BackendDictKeysClient::Uint8Method(
    QVariant value
) {
    QMap<uchar, QString> arg_0;
    arg_0 = value.value<QMap<uchar, QString>>();

    return Uint8Method(
        arg_0
    );
}
Uint8MethodPendingCall* BackendDictKeysClient::Uint8Method(
    QMap<uchar, QString> value
) {
    QDBusArgument dbusvalue;
    dbusvalue << value;
    QDBusInterface iface(
        "com.yarpc.backend",
        "/com/yarpc/backend/dicts",
        "com.yarpc.backend.dictKeys",
        QDBusConnection::sessionBus()
    );
    QDBusPendingCall pendingCall {iface.asyncCall(
        "Uint8Method",
        QVariant::fromValue(dbusvalue)
    )};
    return new Uint8MethodPendingCall(pendingCall, this);
}

Uint8MethodPendingCall::Uint8MethodPendingCall(QDBusPendingCall pendingCall, QObject *parent)
: QObject(parent), m_watcher(pendingCall, this) {
    QObject::connect(
        &m_watcher, &QDBusPendingCallWatcher::finished,
        this, &Uint8MethodPendingCall::callFinished
    );
}

void Uint8MethodPendingCall::callFinished(QDBusPendingCallWatcher *watcher)
{
    QDBusPendingReply<QMap<uchar, QString>> reply {*watcher};
    if (!reply.isValid()) {
        emit error(reply.error());
    } else {
        emit finished(reply);
    }
    deleteLater();
}

BoolMethodPendingCall* BackendDictKeysClient::BoolMethod(
    QVariant value
) {
    QMap<bool, QString> arg_0;
    arg_0 = value.value<QMap<bool, QString>>();

    return BoolMethod(
        arg_0
    );
}
BoolMethodPendingCall* BackendDictKeysClient::BoolMethod(
    QMap<bool, QString> value
) {
    QDBusArgument dbusvalue;
    dbusvalue << value;
    QDBusInterface iface(
        "com.yarpc.backend",
        "/com/yarpc/backend/dicts",
        "com.yarpc.backend.dictKeys",
        QDBusConnection::sessionBus()
    );
    QDBusPendingCall pendingCall {iface.asyncCall(
        "BoolMethod",
        QVariant::fromValue(dbusvalue)
    )};
    return new BoolMethodPendingCall(pendingCall, this);
}

BoolMethodPendingCall::BoolMethodPendingCall(QDBusPendingCall pendingCall, QObject *parent)
: QObject(parent), m_watcher(pendingCall, this) {
    QObject::connect(
        &m_watcher, &QDBusPendingCallWatcher::finished,
        this, &BoolMethodPendingCall::callFinished
    );
}

void BoolMethodPendingCall::callFinished(QDBusPendingCallWatcher *watcher)
{
    QDBusPendingReply<QMap<bool, QString>> reply {*watcher};
    if (!reply.isValid()) {
        emit error(reply.error());
    } else {
        emit finished(reply);
    }
    deleteLater();
}

Int16MethodPendingCall* BackendDictKeysClient::Int16Method(
    QVariant value
) {
    QMap<short, QString> arg_0;
    arg_0 = value.value<QMap<short, QString>>();

    return Int16Method(
        arg_0
    );
}
Int16MethodPendingCall* BackendDictKeysClient::Int16Method(
    QMap<short, QString> value
) {
    QDBusArgument dbusvalue;
    dbusvalue << value;
    QDBusInterface iface(
        "com.yarpc.backend",
        "/com/yarpc/backend/dicts",
        "com.yarpc.backend.dictKeys",
        QDBusConnection::sessionBus()
    );
    QDBusPendingCall pendingCall {iface.asyncCall(
        "Int16Method",
        QVariant::fromValue(dbusvalue)
    )};
    return new Int16MethodPendingCall(pendingCall, this);
}

Int16MethodPendingCall::Int16MethodPendingCall(QDBusPendingCall pendingCall, QObject *parent)
: QObject(parent), m_watcher(pendingCall, this) {
    QObject::connect(
        &m_watcher, &QDBusPendingCallWatcher::finished,
        this, &Int16MethodPendingCall::callFinished
    );
}

void Int16MethodPendingCall::callFinished(QDBusPendingCallWatcher *watcher)
{
    QDBusPendingReply<QMap<short, QString>> reply {*watcher};
    if (!reply.isValid()) {
        emit error(reply.error());
    } else {
        emit finished(reply);
    }
    deleteLater();
}

Uint16MethodPendingCall* BackendDictKeysClient::Uint16Method(
    QVariant value
) {
    QMap<ushort, QString> arg_0;
    arg_0 = value.value<QMap<ushort, QString>>();

    return Uint16Method(
        arg_0
    );
}
Uint16MethodPendingCall* BackendDictKeysClient::Uint16Method(
    QMap<ushort, QString> value
) {
    QDBusArgument dbusvalue;
    dbusvalue << value;
    QDBusInterface iface(
        "com.yarpc.backend",
        "/com/yarpc/backend/dicts",
        "com.yarpc.backend.dictKeys",
        QDBusConnection::sessionBus()
    );
    QDBusPendingCall pendingCall {iface.asyncCall(
        "Uint16Method",
        QVariant::fromValue(dbusvalue)
    )};
    return new Uint16MethodPendingCall(pendingCall, this);
}

Uint16MethodPendingCall::Uint16MethodPendingCall(QDBusPendingCall pendingCall, QObject *parent)
: QObject(parent), m_watcher(pendingCall, this) {
    QObject::connect(
        &m_watcher, &QDBusPendingCallWatcher::finished,
        this, &Uint16MethodPendingCall::callFinished
    );
}

void Uint16MethodPendingCall::callFinished(QDBusPendingCallWatcher *watcher)
{
    QDBusPendingReply<QMap<ushort, QString>> reply {*watcher};
    if (!reply.isValid()) {
        emit error(reply.error());
    } else {
        emit finished(reply);
    }
    deleteLater();
}

Int32MethodPendingCall* BackendDictKeysClient::Int32Method(
    QVariant value
) {
    QMap<int, QString> arg_0;
    arg_0 = value.value<QMap<int, QString>>();

    return Int32Method(
        arg_0
    );
}
Int32MethodPendingCall* BackendDictKeysClient::Int32Method(
    QMap<int, QString> value
) {
    QDBusArgument dbusvalue;
    dbusvalue << value;
    QDBusInterface iface(
        "com.yarpc.backend",
        "/com/yarpc/backend/dicts",
        "com.yarpc.backend.dictKeys",
        QDBusConnection::sessionBus()
    );
    QDBusPendingCall pendingCall {iface.asyncCall(
        "Int32Method",
        QVariant::fromValue(dbusvalue)
    )};
    return new Int32MethodPendingCall(pendingCall, this);
}

Int32MethodPendingCall::Int32MethodPendingCall(QDBusPendingCall pendingCall, QObject *parent)
: QObject(parent), m_watcher(pendingCall, this) {
    QObject::connect(
        &m_watcher, &QDBusPendingCallWatcher::finished,
        this, &Int32MethodPendingCall::callFinished
    );
}

void Int32MethodPendingCall::callFinished(QDBusPendingCallWatcher *watcher)
{
    QDBusPendingReply<QMap<int, QString>> reply {*watcher};
    if (!reply.isValid()) {
        emit error(reply.error());
    } else {
        emit finished(reply);
    }
    deleteLater();
}

Uint32MethodPendingCall* BackendDictKeysClient::Uint32Method(
    QVariant value
) {
    QMap<uint, QString> arg_0;
    arg_0 = value.value<QMap<uint, QString>>();

    return Uint32Method(
        arg_0
    );
}
Uint32MethodPendingCall* BackendDictKeysClient::Uint32Method(
    QMap<uint, QString> value
) {
    QDBusArgument dbusvalue;
    dbusvalue << value;
    QDBusInterface iface(
        "com.yarpc.backend",
        "/com/yarpc/backend/dicts",
        "com.yarpc.backend.dictKeys",
        QDBusConnection::sessionBus()
    );
    QDBusPendingCall pendingCall {iface.asyncCall(
        "Uint32Method",
        QVariant::fromValue(dbusvalue)
    )};
    return new Uint32MethodPendingCall(pendingCall, this);
}

Uint32MethodPendingCall::Uint32MethodPendingCall(QDBusPendingCall pendingCall, QObject *parent)
: QObject(parent), m_watcher(pendingCall, this) {
    QObject::connect(
        &m_watcher, &QDBusPendingCallWatcher::finished,
        this, &Uint32MethodPendingCall::callFinished
    );
}

void Uint32MethodPendingCall::callFinished(QDBusPendingCallWatcher *watcher)
{
    QDBusPendingReply<QMap<uint, QString>> reply {*watcher};
    if (!reply.isValid()) {
        emit error(reply.error());
    } else {
        emit finished(reply);
    }
    deleteLater();
}

Int64MethodPendingCall* BackendDictKeysClient::Int64Method(
    QVariant value
) {
    QMap<qlonglong, QString> arg_0;
    arg_0 = value.value<QMap<qlonglong, QString>>();

    return Int64Method(
        arg_0
    );
}
Int64MethodPendingCall* BackendDictKeysClient::Int64Method(
    QMap<qlonglong, QString> value
) {
    QDBusArgument dbusvalue;
    dbusvalue << value;
    QDBusInterface iface(
        "com.yarpc.backend",
        "/com/yarpc/backend/dicts",
        "com.yarpc.backend.dictKeys",
        QDBusConnection::sessionBus()
    );
    QDBusPendingCall pendingCall {iface.asyncCall(
        "Int64Method",
        QVariant::fromValue(dbusvalue)
    )};
    return new Int64MethodPendingCall(pendingCall, this);
}

Int64MethodPendingCall::Int64MethodPendingCall(QDBusPendingCall pendingCall, QObject *parent)
: QObject(parent), m_watcher(pendingCall, this) {
    QObject::connect(
        &m_watcher, &QDBusPendingCallWatcher::finished,
        this, &Int64MethodPendingCall::callFinished
    );
}

void Int64MethodPendingCall::callFinished(QDBusPendingCallWatcher *watcher)
{
    QDBusPendingReply<QMap<qlonglong, QString>> reply {*watcher};
    if (!reply.isValid()) {
        emit error(reply.error());
    } else {
        emit finished(reply);
    }
    deleteLater();
}

Uint64MethodPendingCall* BackendDictKeysClient::Uint64Method(
    QVariant value
) {
    QMap<qulonglong, QString> arg_0;
    arg_0 = value.value<QMap<qulonglong, QString>>();

    return Uint64Method(
        arg_0
    );
}
Uint64MethodPendingCall* BackendDictKeysClient::Uint64Method(
    QMap<qulonglong, QString> value
) {
    QDBusArgument dbusvalue;
    dbusvalue << value;
    QDBusInterface iface(
        "com.yarpc.backend",
        "/com/yarpc/backend/dicts",
        "com.yarpc.backend.dictKeys",
        QDBusConnection::sessionBus()
    );
    QDBusPendingCall pendingCall {iface.asyncCall(
        "Uint64Method",
        QVariant::fromValue(dbusvalue)
    )};
    return new Uint64MethodPendingCall(pendingCall, this);
}

Uint64MethodPendingCall::Uint64MethodPendingCall(QDBusPendingCall pendingCall, QObject *parent)
: QObject(parent), m_watcher(pendingCall, this) {
    QObject::connect(
        &m_watcher, &QDBusPendingCallWatcher::finished,
        this, &Uint64MethodPendingCall::callFinished
    );
}

void Uint64MethodPendingCall::callFinished(QDBusPendingCallWatcher *watcher)
{
    QDBusPendingReply<QMap<qulonglong, QString>> reply {*watcher};
    if (!reply.isValid()) {
        emit error(reply.error());
    } else {
        emit finished(reply);
    }
    deleteLater();
}

DoubleMethodPendingCall* BackendDictKeysClient::DoubleMethod(
    QVariant value
) {
    QMap<double, QString> arg_0;
    arg_0 = value.value<QMap<double, QString>>();

    return DoubleMethod(
        arg_0
    );
}
DoubleMethodPendingCall* BackendDictKeysClient::DoubleMethod(
    QMap<double, QString> value
) {
    QDBusArgument dbusvalue;
    dbusvalue << value;
    QDBusInterface iface(
        "com.yarpc.backend",
        "/com/yarpc/backend/dicts",
        "com.yarpc.backend.dictKeys",
        QDBusConnection::sessionBus()
    );
    QDBusPendingCall pendingCall {iface.asyncCall(
        "DoubleMethod",
        QVariant::fromValue(dbusvalue)
    )};
    return new DoubleMethodPendingCall(pendingCall, this);
}

DoubleMethodPendingCall::DoubleMethodPendingCall(QDBusPendingCall pendingCall, QObject *parent)
: QObject(parent), m_watcher(pendingCall, this) {
    QObject::connect(
        &m_watcher, &QDBusPendingCallWatcher::finished,
        this, &DoubleMethodPendingCall::callFinished
    );
}

void DoubleMethodPendingCall::callFinished(QDBusPendingCallWatcher *watcher)
{
    QDBusPendingReply<QMap<double, QString>> reply {*watcher};
    if (!reply.isValid()) {
        emit error(reply.error());
    } else {
        emit finished(reply);
    }
    deleteLater();
}

StringMethodPendingCall* BackendDictKeysClient::StringMethod(
    QVariant value
) {
    QMap<QString, QString> arg_0;
    arg_0 = value.value<QMap<QString, QString>>();

    return StringMethod(
        arg_0
    );
}
StringMethodPendingCall* BackendDictKeysClient::StringMethod(
    QMap<QString, QString> value
) {
    QDBusArgument dbusvalue;
    dbusvalue << value;
    QDBusInterface iface(
        "com.yarpc.backend",
        "/com/yarpc/backend/dicts",
        "com.yarpc.backend.dictKeys",
        QDBusConnection::sessionBus()
    );
    QDBusPendingCall pendingCall {iface.asyncCall(
        "StringMethod",
        QVariant::fromValue(dbusvalue)
    )};
    return new StringMethodPendingCall(pendingCall, this);
}

StringMethodPendingCall::StringMethodPendingCall(QDBusPendingCall pendingCall, QObject *parent)
: QObject(parent), m_watcher(pendingCall, this) {
    QObject::connect(
        &m_watcher, &QDBusPendingCallWatcher::finished,
        this, &StringMethodPendingCall::callFinished
    );
}

void StringMethodPendingCall::callFinished(QDBusPendingCallWatcher *watcher)
{
    QDBusPendingReply<QMap<QString, QString>> reply {*watcher};
    if (!reply.isValid()) {
        emit error(reply.error());
    } else {
        emit finished(reply);
    }
    deleteLater();
}

