/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/02.2_primitives.yml
 *   Object: Primitives
 *   Template: qt6/client_source.j2
 */
#include "BackendPrimitivesClient.hpp"
#include "types.hpp"
#include <QDBusConnection>
#include <QDBusInterface>
#include <QDBusReply>
#include <QDBusPendingCall>
#include <QDBusPendingReply>


using namespace gen::with_args;

BackendPrimitivesClient::BackendPrimitivesClient(QObject* parent)
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
        "/com/yarpc/backend/withArgs",
        "com.yarpc.backend.primitives",
        QDBusConnection::sessionBus()
    );
    m_connected = iface.isValid();

    connect(
        &m_watcher, &QDBusServiceWatcher::serviceRegistered,
        this, &BackendPrimitivesClient::connectedHandler
    );
    connect(
        &m_watcher, &QDBusServiceWatcher::serviceUnregistered,
        this, &BackendPrimitivesClient::disconnectedHandler
    );

    QDBusConnection::sessionBus().connect(
        "com.yarpc.backend",
        "/com/yarpc/backend/withArgs",
        "org.freedesktop.DBus.Properties",
        "PropertiesChanged",
        this,
        SLOT(propertiesChangedHandler(QString, QVariantMap, QStringList))
    );
    QDBusConnection::sessionBus().connect(
        "com.yarpc.backend",
        "/com/yarpc/backend/withArgs",
        "com.yarpc.backend.primitives",
        "Uint8Signal",
        this,
        SLOT(Uint8SignalDBusHandler(QDBusMessage))
    );
    QDBusConnection::sessionBus().connect(
        "com.yarpc.backend",
        "/com/yarpc/backend/withArgs",
        "com.yarpc.backend.primitives",
        "BoolSignal",
        this,
        SLOT(BoolSignalDBusHandler(QDBusMessage))
    );
    QDBusConnection::sessionBus().connect(
        "com.yarpc.backend",
        "/com/yarpc/backend/withArgs",
        "com.yarpc.backend.primitives",
        "Int16Signal",
        this,
        SLOT(Int16SignalDBusHandler(QDBusMessage))
    );
    QDBusConnection::sessionBus().connect(
        "com.yarpc.backend",
        "/com/yarpc/backend/withArgs",
        "com.yarpc.backend.primitives",
        "Uint16Signal",
        this,
        SLOT(Uint16SignalDBusHandler(QDBusMessage))
    );
    QDBusConnection::sessionBus().connect(
        "com.yarpc.backend",
        "/com/yarpc/backend/withArgs",
        "com.yarpc.backend.primitives",
        "Int32Signal",
        this,
        SLOT(Int32SignalDBusHandler(QDBusMessage))
    );
    QDBusConnection::sessionBus().connect(
        "com.yarpc.backend",
        "/com/yarpc/backend/withArgs",
        "com.yarpc.backend.primitives",
        "Uint32Signal",
        this,
        SLOT(Uint32SignalDBusHandler(QDBusMessage))
    );
    QDBusConnection::sessionBus().connect(
        "com.yarpc.backend",
        "/com/yarpc/backend/withArgs",
        "com.yarpc.backend.primitives",
        "Int64Signal",
        this,
        SLOT(Int64SignalDBusHandler(QDBusMessage))
    );
    QDBusConnection::sessionBus().connect(
        "com.yarpc.backend",
        "/com/yarpc/backend/withArgs",
        "com.yarpc.backend.primitives",
        "Uint64Signal",
        this,
        SLOT(Uint64SignalDBusHandler(QDBusMessage))
    );
    QDBusConnection::sessionBus().connect(
        "com.yarpc.backend",
        "/com/yarpc/backend/withArgs",
        "com.yarpc.backend.primitives",
        "DoubleSignal",
        this,
        SLOT(DoubleSignalDBusHandler(QDBusMessage))
    );
    QDBusConnection::sessionBus().connect(
        "com.yarpc.backend",
        "/com/yarpc/backend/withArgs",
        "com.yarpc.backend.primitives",
        "StringSignal",
        this,
        SLOT(StringSignalDBusHandler(QDBusMessage))
    );

}

bool BackendPrimitivesClient::getConnected() const {
    return m_connected;
}

QVariantMap BackendPrimitivesClient::getAllProperties() const {
    QDBusInterface iface(
        "com.yarpc.backend",
        "/com/yarpc/backend/withArgs",
        "org.freedesktop.DBus.Properties",
        QDBusConnection::sessionBus()
    );
    QDBusReply<QVariantMap> reply = iface.call(
        "GetAll",
        "com.yarpc.backend.primitives"
    );
    if (!reply.isValid()) {
        return QVariantMap();
    } else {
        return reply.value();
    }
}

void BackendPrimitivesClient::connectedHandler(const QString& service) {
    m_connected = true;
    emit connectedChanged();
}

void BackendPrimitivesClient::disconnectedHandler(const QString& service) {
    m_connected = false;
    emit connectedChanged();
}

void BackendPrimitivesClient::propertiesChangedHandler(QString iface, QVariantMap changes, QStringList) {
    if (iface != "com.yarpc.backend.primitives") {
        return;
    }
}


void BackendPrimitivesClient::Uint8SignalDBusHandler(QDBusMessage content) {
    auto arg_0 = content.arguments()[0].value<uchar>();
    emit uint8SignalReceived(
        QVariant::fromValue(arg_0)
    );
}

void BackendPrimitivesClient::BoolSignalDBusHandler(QDBusMessage content) {
    auto arg_0 = content.arguments()[0].value<bool>();
    emit boolSignalReceived(
        QVariant::fromValue(arg_0)
    );
}

void BackendPrimitivesClient::Int16SignalDBusHandler(QDBusMessage content) {
    auto arg_0 = content.arguments()[0].value<short>();
    emit int16SignalReceived(
        QVariant::fromValue(arg_0)
    );
}

void BackendPrimitivesClient::Uint16SignalDBusHandler(QDBusMessage content) {
    auto arg_0 = content.arguments()[0].value<ushort>();
    emit uint16SignalReceived(
        QVariant::fromValue(arg_0)
    );
}

void BackendPrimitivesClient::Int32SignalDBusHandler(QDBusMessage content) {
    auto arg_0 = content.arguments()[0].value<int>();
    emit int32SignalReceived(
        QVariant::fromValue(arg_0)
    );
}

void BackendPrimitivesClient::Uint32SignalDBusHandler(QDBusMessage content) {
    auto arg_0 = content.arguments()[0].value<uint>();
    emit uint32SignalReceived(
        QVariant::fromValue(arg_0)
    );
}

void BackendPrimitivesClient::Int64SignalDBusHandler(QDBusMessage content) {
    auto arg_0 = content.arguments()[0].value<qlonglong>();
    emit int64SignalReceived(
        QVariant::fromValue(arg_0)
    );
}

void BackendPrimitivesClient::Uint64SignalDBusHandler(QDBusMessage content) {
    auto arg_0 = content.arguments()[0].value<qulonglong>();
    emit uint64SignalReceived(
        QVariant::fromValue(arg_0)
    );
}

void BackendPrimitivesClient::DoubleSignalDBusHandler(QDBusMessage content) {
    auto arg_0 = content.arguments()[0].value<double>();
    emit doubleSignalReceived(
        QVariant::fromValue(arg_0)
    );
}

void BackendPrimitivesClient::StringSignalDBusHandler(QDBusMessage content) {
    auto arg_0 = content.arguments()[0].value<QString>();
    emit stringSignalReceived(
        QVariant::fromValue(arg_0)
    );
}
Uint8MethodPendingCall* BackendPrimitivesClient::Uint8Method(
    QVariant value
) {
    uchar arg_0;
    arg_0 = value.value<uchar>();

    return Uint8Method(
        arg_0
    );
}
Uint8MethodPendingCall* BackendPrimitivesClient::Uint8Method(
    uchar value
) {
    QDBusArgument dbusvalue;
    dbusvalue << value;
    QDBusInterface iface(
        "com.yarpc.backend",
        "/com/yarpc/backend/withArgs",
        "com.yarpc.backend.primitives",
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
    QDBusPendingReply<uchar> reply {*watcher};
    if (!reply.isValid()) {
        emit error(reply.error());
    } else {
        emit finished(reply);
    }
    deleteLater();
}

BoolMethodPendingCall* BackendPrimitivesClient::BoolMethod(
    QVariant value
) {
    bool arg_0;
    arg_0 = value.value<bool>();

    return BoolMethod(
        arg_0
    );
}
BoolMethodPendingCall* BackendPrimitivesClient::BoolMethod(
    bool value
) {
    QDBusArgument dbusvalue;
    dbusvalue << value;
    QDBusInterface iface(
        "com.yarpc.backend",
        "/com/yarpc/backend/withArgs",
        "com.yarpc.backend.primitives",
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
    QDBusPendingReply<bool> reply {*watcher};
    if (!reply.isValid()) {
        emit error(reply.error());
    } else {
        emit finished(reply);
    }
    deleteLater();
}

Int16MethodPendingCall* BackendPrimitivesClient::Int16Method(
    QVariant value
) {
    short arg_0;
    arg_0 = value.value<short>();

    return Int16Method(
        arg_0
    );
}
Int16MethodPendingCall* BackendPrimitivesClient::Int16Method(
    short value
) {
    QDBusArgument dbusvalue;
    dbusvalue << value;
    QDBusInterface iface(
        "com.yarpc.backend",
        "/com/yarpc/backend/withArgs",
        "com.yarpc.backend.primitives",
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
    QDBusPendingReply<short> reply {*watcher};
    if (!reply.isValid()) {
        emit error(reply.error());
    } else {
        emit finished(reply);
    }
    deleteLater();
}

Uint16MethodPendingCall* BackendPrimitivesClient::Uint16Method(
    QVariant value
) {
    ushort arg_0;
    arg_0 = value.value<ushort>();

    return Uint16Method(
        arg_0
    );
}
Uint16MethodPendingCall* BackendPrimitivesClient::Uint16Method(
    ushort value
) {
    QDBusArgument dbusvalue;
    dbusvalue << value;
    QDBusInterface iface(
        "com.yarpc.backend",
        "/com/yarpc/backend/withArgs",
        "com.yarpc.backend.primitives",
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
    QDBusPendingReply<ushort> reply {*watcher};
    if (!reply.isValid()) {
        emit error(reply.error());
    } else {
        emit finished(reply);
    }
    deleteLater();
}

Int32MethodPendingCall* BackendPrimitivesClient::Int32Method(
    QVariant value
) {
    int arg_0;
    arg_0 = value.value<int>();

    return Int32Method(
        arg_0
    );
}
Int32MethodPendingCall* BackendPrimitivesClient::Int32Method(
    int value
) {
    QDBusArgument dbusvalue;
    dbusvalue << value;
    QDBusInterface iface(
        "com.yarpc.backend",
        "/com/yarpc/backend/withArgs",
        "com.yarpc.backend.primitives",
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
    QDBusPendingReply<int> reply {*watcher};
    if (!reply.isValid()) {
        emit error(reply.error());
    } else {
        emit finished(reply);
    }
    deleteLater();
}

Uint32MethodPendingCall* BackendPrimitivesClient::Uint32Method(
    QVariant value
) {
    uint arg_0;
    arg_0 = value.value<uint>();

    return Uint32Method(
        arg_0
    );
}
Uint32MethodPendingCall* BackendPrimitivesClient::Uint32Method(
    uint value
) {
    QDBusArgument dbusvalue;
    dbusvalue << value;
    QDBusInterface iface(
        "com.yarpc.backend",
        "/com/yarpc/backend/withArgs",
        "com.yarpc.backend.primitives",
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
    QDBusPendingReply<uint> reply {*watcher};
    if (!reply.isValid()) {
        emit error(reply.error());
    } else {
        emit finished(reply);
    }
    deleteLater();
}

Int64MethodPendingCall* BackendPrimitivesClient::Int64Method(
    QVariant value
) {
    qlonglong arg_0;
    arg_0 = value.value<qlonglong>();

    return Int64Method(
        arg_0
    );
}
Int64MethodPendingCall* BackendPrimitivesClient::Int64Method(
    qlonglong value
) {
    QDBusArgument dbusvalue;
    dbusvalue << value;
    QDBusInterface iface(
        "com.yarpc.backend",
        "/com/yarpc/backend/withArgs",
        "com.yarpc.backend.primitives",
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
    QDBusPendingReply<qlonglong> reply {*watcher};
    if (!reply.isValid()) {
        emit error(reply.error());
    } else {
        emit finished(reply);
    }
    deleteLater();
}

Uint64MethodPendingCall* BackendPrimitivesClient::Uint64Method(
    QVariant value
) {
    qulonglong arg_0;
    arg_0 = value.value<qulonglong>();

    return Uint64Method(
        arg_0
    );
}
Uint64MethodPendingCall* BackendPrimitivesClient::Uint64Method(
    qulonglong value
) {
    QDBusArgument dbusvalue;
    dbusvalue << value;
    QDBusInterface iface(
        "com.yarpc.backend",
        "/com/yarpc/backend/withArgs",
        "com.yarpc.backend.primitives",
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
    QDBusPendingReply<qulonglong> reply {*watcher};
    if (!reply.isValid()) {
        emit error(reply.error());
    } else {
        emit finished(reply);
    }
    deleteLater();
}

DoubleMethodPendingCall* BackendPrimitivesClient::DoubleMethod(
    QVariant value
) {
    double arg_0;
    arg_0 = value.value<double>();

    return DoubleMethod(
        arg_0
    );
}
DoubleMethodPendingCall* BackendPrimitivesClient::DoubleMethod(
    double value
) {
    QDBusArgument dbusvalue;
    dbusvalue << value;
    QDBusInterface iface(
        "com.yarpc.backend",
        "/com/yarpc/backend/withArgs",
        "com.yarpc.backend.primitives",
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
    QDBusPendingReply<double> reply {*watcher};
    if (!reply.isValid()) {
        emit error(reply.error());
    } else {
        emit finished(reply);
    }
    deleteLater();
}

StringMethodPendingCall* BackendPrimitivesClient::StringMethod(
    QVariant value
) {
    QString arg_0;
    arg_0 = value.value<QString>();

    return StringMethod(
        arg_0
    );
}
StringMethodPendingCall* BackendPrimitivesClient::StringMethod(
    QString value
) {
    QDBusArgument dbusvalue;
    dbusvalue << value;
    QDBusInterface iface(
        "com.yarpc.backend",
        "/com/yarpc/backend/withArgs",
        "com.yarpc.backend.primitives",
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
    QDBusPendingReply<QString> reply {*watcher};
    if (!reply.isValid()) {
        emit error(reply.error());
    } else {
        emit finished(reply);
    }
    deleteLater();
}

