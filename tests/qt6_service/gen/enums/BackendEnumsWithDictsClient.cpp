/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/06.3_enums_with_dicts.yml
 *   Object: EnumsWithDicts
 *   Template: qt6/client_source.j2
 */
#include "BackendEnumsWithDictsClient.hpp"
#include <QDBusConnection>
#include <QDBusInterface>
#include <QDBusReply>
#include <QDBusPendingCall>
#include <QDBusPendingReply>

using namespace gen::enums;

BackendEnumsWithDictsClient::BackendEnumsWithDictsClient(QObject* parent)
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
        "com.yarpc.backend.enumsWithDicts",
        QDBusConnection::sessionBus()
    );
    m_connected = iface.isValid();

    connect(
        &m_watcher, &QDBusServiceWatcher::serviceRegistered,
        this, &BackendEnumsWithDictsClient::connectedHandler
    );
    connect(
        &m_watcher, &QDBusServiceWatcher::serviceUnregistered,
        this, &BackendEnumsWithDictsClient::disconnectedHandler
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
        "com.yarpc.backend.enumsWithDicts",
        "EnumSignal",
        this,
        SLOT(EnumSignalDBusHandler(QDBusMessage))
    );

}

bool BackendEnumsWithDictsClient::getConnected() const {
    return m_connected;
}

QVariantMap BackendEnumsWithDictsClient::getAllProperties() const {
    QDBusInterface iface(
        "com.yarpc.backend",
        "/com/yarpc/backend/enums",
        "org.freedesktop.DBus.Properties",
        QDBusConnection::sessionBus()
    );
    QDBusReply<QVariantMap> reply = iface.call(
        "GetAll",
        "com.yarpc.backend.enumsWithDicts"
    );
    if (!reply.isValid()) {
        return QVariantMap();
    } else {
        return reply.value();
    }
}

void BackendEnumsWithDictsClient::connectedHandler(const QString& service) {
    m_connected = true;
    emit connectedChanged();
}

void BackendEnumsWithDictsClient::disconnectedHandler(const QString& service) {
    m_connected = false;
    emit connectedChanged();
}

void BackendEnumsWithDictsClient::propertiesChangedHandler(QString iface, QVariantMap changes, QStringList) {
    if (iface != "com.yarpc.backend.enumsWithDicts") {
        return;
    }
    if (changes.contains("EnumProperty")) {
        emit enumPropertyChanged();
    }
}

EnumMethodPendingCall* BackendEnumsWithDictsClient::EnumMethod(
    QMap<$1, $2> color
) {
    QDBusArgument dbuscolor;
    dbuscolor << color;
    QDBusInterface iface(
        "com.yarpc.backend",
        "/com/yarpc/backend/enums",
        "com.yarpc.backend.enumsWithDicts",
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
    QDBusPendingReply<QMap<$1, $2>> reply {*watcher};
    if (!reply.isValid()) {
        emit error(reply.error());
    } else {
        emit finished(reply);
    }
    deleteLater();
}


void BackendEnumsWithDictsClient::EnumSignalDBusHandler(QDBusMessage content) {
    emit enumSignalReceived(
        content.arguments()[0].value<QMap<$1, $2>>()
    );
}


QMap<$1, $2> BackendEnumsWithDictsClient::getEnumProperty() const {
    QDBusInterface iface(
        "com.yarpc.backend",
        "/com/yarpc/backend/enums",
        "com.yarpc.backend.enumsWithDicts",
        QDBusConnection::sessionBus()
    );
    return iface.property("EnumProperty").value<QMap<$1, $2>>();
}

void BackendEnumsWithDictsClient::setEnumProperty(const QMap<$1, $2> &newValue) {
    QDBusInterface iface(
        "com.yarpc.backend",
        "/com/yarpc/backend/enums",
        "com.yarpc.backend.enumsWithDicts",
        QDBusConnection::sessionBus()
    );
    iface.setProperty("EnumProperty", newValue);
}
