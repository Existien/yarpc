/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/01_minimal.yml
 *   Object: Minimal
 *   Template: qt6/client_source.j2
 */
#include "BackendMinimalClient.hpp"
#include "types.hpp"
#include <QDBusConnection>
#include <QDBusInterface>
#include <QDBusReply>
#include <QDBusPendingCall>
#include <QDBusPendingReply>


using namespace gen::minimal;
using namespace BackendMinimalClientUtils;

BackendMinimalClient::BackendMinimalClient(QObject* parent)
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
        "/com/yarpc/backend/minimal",
        "com.yarpc.backend.minimal",
        QDBusConnection::sessionBus()
    );
    m_connected = iface.isValid();

    connect(
        &m_watcher, &QDBusServiceWatcher::serviceRegistered,
        this, &BackendMinimalClient::connectedHandler
    );
    connect(
        &m_watcher, &QDBusServiceWatcher::serviceUnregistered,
        this, &BackendMinimalClient::disconnectedHandler
    );

    QDBusConnection::sessionBus().connect(
        "com.yarpc.backend",
        "/com/yarpc/backend/minimal",
        "org.freedesktop.DBus.Properties",
        "PropertiesChanged",
        this,
        SLOT(propertiesChangedHandler(QString, QVariantMap, QStringList))
    );
    QDBusConnection::sessionBus().connect(
        "com.yarpc.backend",
        "/com/yarpc/backend/minimal",
        "com.yarpc.backend.minimal",
        "Bumped",
        this,
        SLOT(BumpedDBusHandler(QDBusMessage))
    );

}

bool BackendMinimalClient::getConnected() const {
    return m_connected;
}

QVariantMap BackendMinimalClient::getAllProperties() const {
    QDBusInterface iface(
        "com.yarpc.backend",
        "/com/yarpc/backend/minimal",
        "org.freedesktop.DBus.Properties",
        QDBusConnection::sessionBus()
    );
    QDBusReply<QVariantMap> reply = iface.call(
        "GetAll",
        "com.yarpc.backend.minimal"
    );
    if (!reply.isValid()) {
        return QVariantMap();
    } else {
        return reply.value();
    }
}

void BackendMinimalClient::connectedHandler(const QString& service) {
    m_connected = true;
    emit connectedChanged();
}

void BackendMinimalClient::disconnectedHandler(const QString& service) {
    m_connected = false;
    emit connectedChanged();
}

void BackendMinimalClient::propertiesChangedHandler(QString iface, QVariantMap changes, QStringList) {
    if (iface != "com.yarpc.backend.minimal") {
        return;
    }
}


void BackendMinimalClient::BumpedDBusHandler(QDBusMessage content) {
    emit bumpedReceived(

    );
}
BumpPendingCall* BackendMinimalClient::Bump(
    
) {
    QDBusInterface iface(
        "com.yarpc.backend",
        "/com/yarpc/backend/minimal",
        "com.yarpc.backend.minimal",
        QDBusConnection::sessionBus()
    );
    QDBusPendingCall pendingCall {iface.asyncCall(
        "Bump"
    )};
    return new BumpPendingCall(pendingCall, this);
}

BumpPendingCall::BumpPendingCall(QDBusPendingCall pendingCall, QObject *parent)
: QObject(parent), m_watcher(pendingCall, this) {
    QObject::connect(
        &m_watcher, &QDBusPendingCallWatcher::finished,
        this, &BumpPendingCall::callFinished
    );
}

void BumpPendingCall::callFinished(QDBusPendingCallWatcher *watcher)
{
    QDBusPendingReply<void> reply {*watcher};
    if (!reply.isValid()) {
        emit error(reply.error());
    } else {
        emit finished();
    }
    deleteLater();
}

