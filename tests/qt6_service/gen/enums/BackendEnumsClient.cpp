/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/06.1_enums.yml
 *   Object: Enums
 *   Template: qt6/client_source.j2
 */
#include "BackendEnumsClient.hpp"
#include <QDBusConnection>
#include <QDBusInterface>
#include <QDBusReply>
#include <QDBusPendingCall>
#include <QDBusPendingReply>

using namespace gen::enums;

BackendEnumsClient::BackendEnumsClient(QObject* parent)
 : QObject(parent),
   m_watcher(QDBusServiceWatcher(
    "com.yarpc.backend",
    QDBusConnection::sessionBus(),
    QDBusServiceWatcher::WatchForRegistration | QDBusServiceWatcher::WatchForUnregistration,
    parent
   ))
{

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
     color
) {
    QDBusArgument dbuscolor;
    dbuscolor << color;
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
    QDBusPendingReply<> reply {*watcher};
    if (!reply.isValid()) {
        emit error(reply.error());
    } else {
        emit finished(reply);
    }
    deleteLater();
}


void BackendEnumsClient::EnumSignalDBusHandler(QDBusMessage content) {
    emit enumSignalReceived(
        content.arguments()[0].value<>()
    );
}


 BackendEnumsClient::getEnumProperty() const {
    QDBusInterface iface(
        "com.yarpc.backend",
        "/com/yarpc/backend/enums",
        "com.yarpc.backend.enums",
        QDBusConnection::sessionBus()
    );
    return iface.property("EnumProperty").value<>();
}

void BackendEnumsClient::setEnumProperty(const  &newValue) {
    QDBusInterface iface(
        "com.yarpc.backend",
        "/com/yarpc/backend/enums",
        "com.yarpc.backend.enums",
        QDBusConnection::sessionBus()
    );
    iface.setProperty("EnumProperty", newValue);
}
