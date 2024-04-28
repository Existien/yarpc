/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/05.2_dictionaries_with_structs.yml
 *   Object: DictsWithStructs
 *   Template: qt6/client_source.j2
 */
#include "BackendDictsWithStructsClient.hpp"
#include <QDBusConnection>
#include <QDBusInterface>
#include <QDBusReply>
#include <QDBusPendingCall>
#include <QDBusPendingReply>

using namespace gen::dicts;

BackendDictsWithStructsClient::BackendDictsWithStructsClient(QObject* parent)
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
        "/com/yarpc/backend",
        "com.yarpc.backend.dictsWithStructs",
        QDBusConnection::sessionBus()
    );
    m_connected = iface.isValid();

    connect(
        &m_watcher, &QDBusServiceWatcher::serviceRegistered,
        this, &BackendDictsWithStructsClient::connectedHandler
    );
    connect(
        &m_watcher, &QDBusServiceWatcher::serviceUnregistered,
        this, &BackendDictsWithStructsClient::disconnectedHandler
    );

    QDBusConnection::sessionBus().connect(
        "com.yarpc.backend",
        "/com/yarpc/backend",
        "com.yarpc.backend.dictsWithStructs",
        "DictStructSignal",
        this,
        SLOT(DictStructSignalDBusHandler(QDBusMessage))
    );

}

bool BackendDictsWithStructsClient::getConnected() const {
    return m_connected;
}

void BackendDictsWithStructsClient::connectedHandler(const QString& service) {
    m_connected = true;
    emit connectedChanged();
}

void BackendDictsWithStructsClient::disconnectedHandler(const QString& service) {
    m_connected = false;
    emit connectedChanged();
}

DictsStructMethodPendingCall* BackendDictsWithStructsClient::DictsStructMethod() {
    QDBusInterface iface(
        "com.yarpc.backend",
        "/com/yarpc/backend",
        "com.yarpc.backend.dictsWithStructs",
        QDBusConnection::sessionBus()
    );
    QDBusPendingCall pendingCall {iface.asyncCall(
        "DictsStructMethod"
    )};
    return new DictsStructMethodPendingCall(pendingCall, this);
}

DictsStructMethodPendingCall::DictsStructMethodPendingCall(QDBusPendingCall pendingCall, QObject *parent)
: QObject(parent), m_watcher(pendingCall, this) {
    QObject::connect(
        &m_watcher, &QDBusPendingCallWatcher::finished,
        this, &DictsStructMethodPendingCall::callFinished
    );
}

void DictsStructMethodPendingCall::callFinished(QDBusPendingCallWatcher *watcher)
{
    QDBusPendingReply<void> reply {*watcher};
    if (!reply.isValid()) {
        emit error(reply.error());
    } else {
        emit finished();
    }
    deleteLater();
}


void BackendDictsWithStructsClient::DictStructSignalDBusHandler(QDBusMessage content) {
    emit dictStructSignalReceived();
}

