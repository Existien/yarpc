/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/06.1_enums.yml
 *   Object: Enums
 *   Template: qt6/client_source.j2
 */
#include "BackendEnumsClient.hpp"
#include "types.hpp"
#include <QDBusConnection>
#include <QDBusInterface>
#include <QDBusReply>
#include <QDBusPendingCall>
#include <QDBusPendingReply>


using namespace gen::enums;
using namespace BackendEnumsClientUtils;

BackendEnumsClient::BackendEnumsClient(QObject* parent)
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
        "/com/yarpc/backend/enums",
        "com.yarpc.backend.enums",
        QDBusConnection::sessionBus()
    );
    m_connected = iface.isValid();

    connect(
        &m_watcher, &QDBusServiceWatcher::serviceRegistered,
        this, &BackendEnumsClient::connectedHandler
    );
    connect(
        &m_watcher, &QDBusServiceWatcher::serviceUnregistered,
        this, &BackendEnumsClient::disconnectedHandler
    );

    QDBusConnection::sessionBus().connect(
        "com.yarpc.backend",
        "/com/yarpc/backend/enums",
        "org.freedesktop.DBus.Properties",
        "PropertiesChanged",
        this,
        SLOT(propertiesChangedHandler(QString, QVariantMap, QStringList))
    );
    QDBusConnection::sessionBus().connect(
        "com.yarpc.backend",
        "/com/yarpc/backend/enums",
        "com.yarpc.backend.enums",
        "EnumSignal",
        this,
        SLOT(EnumSignalDBusHandler(QDBusMessage))
    );

}

bool BackendEnumsClient::getConnected() const {
    return m_connected;
}

QVariantMap BackendEnumsClient::getAllProperties() const {
    QDBusInterface iface(
        "com.yarpc.backend",
        "/com/yarpc/backend/enums",
        "org.freedesktop.DBus.Properties",
        QDBusConnection::sessionBus()
    );
    QDBusReply<QVariantMap> reply = iface.call(
        "GetAll",
        "com.yarpc.backend.enums"
    );
    if (!reply.isValid()) {
        return QVariantMap();
    } else {
        return reply.value();
    }
}

void BackendEnumsClient::connectedHandler(const QString& service) {
    m_connected = true;
    emit connectedChanged();
}

void BackendEnumsClient::disconnectedHandler(const QString& service) {
    m_connected = false;
    emit connectedChanged();
}

void BackendEnumsClient::propertiesChangedHandler(QString iface, QVariantMap changes, QStringList) {
    if (iface != "com.yarpc.backend.enums") {
        return;
    }
    if (changes.contains("EnumProperty")) {
        emit enumPropertyChanged();
    }
}

EnumMethodPendingCall* BackendEnumsClient::EnumMethod(
    QVariant color
) {
    Color::Type arg_0;
    arg_0 = color.value<Color::Type>();

    return EnumMethod(
        arg_0
    );
}
EnumMethodPendingCall* BackendEnumsClient::EnumMethod(
    Color::Type color
) {
    QDBusArgument dbuscolor;
    dbuscolor << *reinterpret_cast<const int*>(&color);
    QDBusInterface iface(
        "com.yarpc.backend",
        "/com/yarpc/backend/enums",
        "com.yarpc.backend.enums",
        QDBusConnection::sessionBus()
    );
    QDBusPendingCall pendingCall {iface.asyncCall(
        "EnumMethod",
        QVariant::fromValue(dbuscolor)
    )};
    return new EnumMethodPendingCall(pendingCall, this);
}

EnumMethodPendingCall::EnumMethodPendingCall(QDBusPendingCall pendingCall, QObject *parent)
: QObject(parent), m_watcher(pendingCall, this) {
    QObject::connect(
        &m_watcher, &QDBusPendingCallWatcher::finished,
        this, &EnumMethodPendingCall::callFinished
    );
}

void EnumMethodPendingCall::callFinished(QDBusPendingCallWatcher *watcher)
{
    QDBusPendingReply<int> reply {*watcher};
    if (!reply.isValid()) {
        emit error(reply.error());
    } else {
        int finishedReply = reply;
        emit finished(*reinterpret_cast<const Color::Type*>(&finishedReply));
    }
    deleteLater();
}


void BackendEnumsClient::EnumSignalDBusHandler(QDBusMessage content) {
    auto arg_0 = content.arguments()[0].value<Color::Type>();
    emit enumSignalReceived(
        QVariant::fromValue(arg_0)
    );
}


Color::Type BackendEnumsClient::getEnumProperty() const {
    QDBusInterface iface(
        "com.yarpc.backend",
        "/com/yarpc/backend/enums",
        "org.freedesktop.DBus.Properties",
        QDBusConnection::sessionBus()
    );
    QDBusReply<QDBusVariant> reply = iface.call(
        "Get",
        "com.yarpc.backend.enums",
        "EnumProperty"
    );
    Color::Type unmarshalled{};
    if (reply.isValid()) {
        unmarshalled = reply.value().variant().value<Color::Type>();
    }
    return unmarshalled;
}


QVariant BackendEnumsClient::getVariantEnumProperty() const {
    auto unmarshalled = getEnumProperty();
    QVariant marshalled;
    marshalled = QVariant::fromValue(unmarshalled);

    return marshalled;
}


void BackendEnumsClient::setEnumProperty(const Color::Type &newValue) {
    QDBusInterface iface(
        "com.yarpc.backend",
        "/com/yarpc/backend/enums",
        "org.freedesktop.DBus.Properties",
        QDBusConnection::sessionBus()
    );
    QDBusArgument marshalled;
    QDBusVariant v;
    v.setVariant(QVariant::fromValue(*reinterpret_cast<const int*>(&newValue)));
    marshalled << v;
    iface.call(
        "Set",
        "com.yarpc.backend.enums",
        "EnumProperty",
        QVariant::fromValue<QDBusArgument>(marshalled)
    );
}

void BackendEnumsClient::setVariantEnumProperty(QVariant value ) {
    Color::Type unmarshalled;
    unmarshalled = value.value<Color::Type>();

    setEnumProperty(unmarshalled);
}
