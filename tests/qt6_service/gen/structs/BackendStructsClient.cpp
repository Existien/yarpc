/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/03_structs.yml
 *   Object: Structs
 *   Template: qt6/client_source.j2
 */
#include "BackendStructsClient.hpp"
#include "types.hpp"
#include <QDBusConnection>
#include <QDBusInterface>
#include <QDBusReply>
#include <QDBusPendingCall>
#include <QDBusPendingReply>


using namespace gen::structs;
using namespace BackendStructsClientUtils;

BackendStructsClient::BackendStructsClient(QObject* parent)
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
        "/com/yarpc/backend/structs",
        "com.yarpc.backend.structs",
        QDBusConnection::sessionBus()
    );
    m_connected = iface.isValid();

    connect(
        &m_watcher, &QDBusServiceWatcher::serviceRegistered,
        this, &BackendStructsClient::connectedHandler
    );
    connect(
        &m_watcher, &QDBusServiceWatcher::serviceUnregistered,
        this, &BackendStructsClient::disconnectedHandler
    );

    QDBusConnection::sessionBus().connect(
        "com.yarpc.backend",
        "/com/yarpc/backend/structs",
        "org.freedesktop.DBus.Properties",
        "PropertiesChanged",
        this,
        SLOT(propertiesChangedHandler(QString, QVariantMap, QStringList))
    );
    QDBusConnection::sessionBus().connect(
        "com.yarpc.backend",
        "/com/yarpc/backend/structs",
        "com.yarpc.backend.structs",
        "StructReceived",
        this,
        SLOT(StructReceivedDBusHandler(QDBusMessage))
    );

}

bool BackendStructsClient::getConnected() const {
    return m_connected;
}

QVariantMap BackendStructsClient::getAllProperties() const {
    QDBusInterface iface(
        "com.yarpc.backend",
        "/com/yarpc/backend/structs",
        "org.freedesktop.DBus.Properties",
        QDBusConnection::sessionBus()
    );
    QDBusReply<QVariantMap> reply = iface.call(
        "GetAll",
        "com.yarpc.backend.structs"
    );
    if (!reply.isValid()) {
        return QVariantMap();
    } else {
        return reply.value();
    }
}

void BackendStructsClient::connectedHandler(const QString& service) {
    m_connected = true;
    emit connectedChanged();
}

void BackendStructsClient::disconnectedHandler(const QString& service) {
    m_connected = false;
    emit connectedChanged();
}

void BackendStructsClient::propertiesChangedHandler(QString iface, QVariantMap changes, QStringList) {
    if (iface != "com.yarpc.backend.structs") {
        return;
    }
    if (changes.contains("Simple")) {
        emit simpleChanged();
    }
}

SendStructPendingCall* BackendStructsClient::SendStruct(
    QVariant simpleStruct
) {
    SimpleStruct arg_0;
    arg_0 = simpleStruct.value<SimpleStruct>();

    return SendStruct(
        arg_0
    );
}
SendStructPendingCall* BackendStructsClient::SendStruct(
    SimpleStruct simpleStruct
) {
    QDBusArgument dbussimpleStruct;
    dbussimpleStruct << simpleStruct;
    QDBusInterface iface(
        "com.yarpc.backend",
        "/com/yarpc/backend/structs",
        "com.yarpc.backend.structs",
        QDBusConnection::sessionBus()
    );
    QDBusPendingCall pendingCall {iface.asyncCall(
        "SendStruct",
        QVariant::fromValue(dbussimpleStruct)
    )};
    return new SendStructPendingCall(pendingCall, this);
}

SendStructPendingCall::SendStructPendingCall(QDBusPendingCall pendingCall, QObject *parent)
: QObject(parent), m_watcher(pendingCall, this) {
    QObject::connect(
        &m_watcher, &QDBusPendingCallWatcher::finished,
        this, &SendStructPendingCall::callFinished
    );
}

void SendStructPendingCall::callFinished(QDBusPendingCallWatcher *watcher)
{
    QDBusPendingReply<SimpleStruct> reply {*watcher};
    if (!reply.isValid()) {
        emit error(reply.error());
    } else {
        SimpleStruct finishedReply = reply;
        emit finished(finishedReply);
    }
    deleteLater();
}


void BackendStructsClient::StructReceivedDBusHandler(QDBusMessage content) {
    SimpleStruct arg_0;
    content.arguments()[0].value<QDBusArgument>() >> arg_0;
    auto arg_1 = content.arguments()[1].value<double>();
    emit structReceivedReceived(
        QVariant::fromValue(arg_0),
        QVariant::fromValue(arg_1)
    );
}


SimpleStruct BackendStructsClient::getSimple() const {
    QDBusInterface iface(
        "com.yarpc.backend",
        "/com/yarpc/backend/structs",
        "org.freedesktop.DBus.Properties",
        QDBusConnection::sessionBus()
    );
    QDBusReply<QDBusVariant> reply = iface.call(
        "Get",
        "com.yarpc.backend.structs",
        "Simple"
    );
    SimpleStruct unmarshalled{};
    if (reply.isValid()) {
        auto marshalled = qvariant_cast<QDBusArgument>(reply.value().variant());
        marshalled >> unmarshalled;
    }
    return unmarshalled;
}


QVariant BackendStructsClient::getVariantSimple() const {
    auto unmarshalled = getSimple();
    QVariant marshalled;
    marshalled = QVariant::fromValue(unmarshalled);

    return marshalled;
}


void BackendStructsClient::setSimple(const SimpleStruct &newValue) {
    QDBusInterface iface(
        "com.yarpc.backend",
        "/com/yarpc/backend/structs",
        "org.freedesktop.DBus.Properties",
        QDBusConnection::sessionBus()
    );
    QDBusArgument marshalled;
    QDBusVariant v;
    v.setVariant(QVariant::fromValue(newValue));
    marshalled << v;
    iface.call(
        "Set",
        "com.yarpc.backend.structs",
        "Simple",
        QVariant::fromValue<QDBusArgument>(marshalled)
    );
}

void BackendStructsClient::setVariantSimple(QVariant value ) {
    SimpleStruct unmarshalled;
    unmarshalled = value.value<SimpleStruct>();

    setSimple(unmarshalled);
}
