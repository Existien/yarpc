/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/05.1_dictionaries.yml
 *   Object: Dicts
 *   Template: qt6/client_source.j2
 */
#include "BackendDictsClient.hpp"
#include <QDBusConnection>
#include <QDBusInterface>
#include <QDBusReply>
#include <QDBusPendingCall>
#include <QDBusPendingReply>

using namespace gen::dicts;

BackendDictsClient::BackendDictsClient(QObject* parent)
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
        "/com/yarpc/backend/dicts",
        "com.yarpc.backend.dicts",
        QDBusConnection::sessionBus()
    );
    m_connected = iface.isValid();

    connect(
        &m_watcher, &QDBusServiceWatcher::serviceRegistered,
        this, &BackendDictsClient::connectedHandler
    );
    connect(
        &m_watcher, &QDBusServiceWatcher::serviceUnregistered,
        this, &BackendDictsClient::disconnectedHandler
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
        "com.yarpc.backend.dicts",
        "DictSignal",
        this,
        SLOT(DictSignalDBusHandler(QDBusMessage))
    );

}

bool BackendDictsClient::getConnected() const {
    return m_connected;
}

QVariantMap BackendDictsClient::getAllProperties() const {
    QDBusInterface iface(
        "com.yarpc.backend",
        "/com/yarpc/backend/dicts",
        "org.freedesktop.DBus.Properties",
        QDBusConnection::sessionBus()
    );
    QDBusReply<QVariantMap> reply = iface.call(
        "GetAll",
        "com.yarpc.backend.dicts"
    );
    if (!reply.isValid()) {
        return QVariantMap();
    } else {
        return reply.value();
    }
}

void BackendDictsClient::connectedHandler(const QString& service) {
    m_connected = true;
    emit connectedChanged();
}

void BackendDictsClient::disconnectedHandler(const QString& service) {
    m_connected = false;
    emit connectedChanged();
}

void BackendDictsClient::propertiesChangedHandler(QString iface, QVariantMap changes, QStringList) {
    if (iface != "com.yarpc.backend.dicts") {
        return;
    }
    if (changes.contains("DictProperty")) {
        emit dictPropertyChanged();
    }
}

DictMethodPendingCall* BackendDictsClient::DictMethod(
    QMap<$1, $2> keysNValues
) {
    QDBusArgument dbuskeysNValues;
    dbuskeysNValues << keysNValues;
    QDBusInterface iface(
        "com.yarpc.backend",
        "/com/yarpc/backend/dicts",
        "com.yarpc.backend.dicts",
        QDBusConnection::sessionBus()
    );
    QDBusPendingCall pendingCall {iface.asyncCall(
        "DictMethod",
        QVariant::fromValue(dbuskeysNValues)
    )};
    return new DictMethodPendingCall(pendingCall, this);
}

DictMethodPendingCall::DictMethodPendingCall(QDBusPendingCall pendingCall, QObject *parent)
: QObject(parent), m_watcher(pendingCall, this) {
    QObject::connect(
        &m_watcher, &QDBusPendingCallWatcher::finished,
        this, &DictMethodPendingCall::callFinished
    );
}

void DictMethodPendingCall::callFinished(QDBusPendingCallWatcher *watcher)
{
    QDBusPendingReply<QMap<$1, $2>> reply {*watcher};
    if (!reply.isValid()) {
        emit error(reply.error());
    } else {
        emit finished(reply);
    }
    deleteLater();
}


void BackendDictsClient::DictSignalDBusHandler(QDBusMessage content) {
    emit dictSignalReceived(
        content.arguments()[0].value<QMap<$1, $2>>()
    );
}


QMap<$1, $2> BackendDictsClient::getDictProperty() const {
    QDBusInterface iface(
        "com.yarpc.backend",
        "/com/yarpc/backend/dicts",
        "com.yarpc.backend.dicts",
        QDBusConnection::sessionBus()
    );
    return iface.property("DictProperty").value<QMap<$1, $2>>();
}

void BackendDictsClient::setDictProperty(const QMap<$1, $2> &newValue) {
    QDBusInterface iface(
        "com.yarpc.backend",
        "/com/yarpc/backend/dicts",
        "com.yarpc.backend.dicts",
        QDBusConnection::sessionBus()
    );
    iface.setProperty("DictProperty", newValue);
}
