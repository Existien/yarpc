/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/05.3_dictionaries_with_arrays.yml
 *   Object: DictsWithArrays
 *   Template: qt6/client_source.j2
 */
#include "BackendDictsWithArraysClient.hpp"
#include "types.hpp"
#include <QDBusConnection>
#include <QDBusInterface>
#include <QDBusReply>
#include <QDBusPendingCall>
#include <QDBusPendingReply>


using namespace gen::dicts;

BackendDictsWithArraysClient::BackendDictsWithArraysClient(QObject* parent)
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
        "com.yarpc.backend.dictsWithArrays",
        QDBusConnection::sessionBus()
    );
    m_connected = iface.isValid();

    connect(
        &m_watcher, &QDBusServiceWatcher::serviceRegistered,
        this, &BackendDictsWithArraysClient::connectedHandler
    );
    connect(
        &m_watcher, &QDBusServiceWatcher::serviceUnregistered,
        this, &BackendDictsWithArraysClient::disconnectedHandler
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
        "com.yarpc.backend.dictsWithArrays",
        "DictsArraySignal",
        this,
        SLOT(DictsArraySignalDBusHandler(QDBusMessage))
    );

}

bool BackendDictsWithArraysClient::getConnected() const {
    return m_connected;
}

QVariantMap BackendDictsWithArraysClient::getAllProperties() const {
    QDBusInterface iface(
        "com.yarpc.backend",
        "/com/yarpc/backend/dicts",
        "org.freedesktop.DBus.Properties",
        QDBusConnection::sessionBus()
    );
    QDBusReply<QVariantMap> reply = iface.call(
        "GetAll",
        "com.yarpc.backend.dictsWithArrays"
    );
    if (!reply.isValid()) {
        return QVariantMap();
    } else {
        return reply.value();
    }
}

void BackendDictsWithArraysClient::connectedHandler(const QString& service) {
    m_connected = true;
    emit connectedChanged();
}

void BackendDictsWithArraysClient::disconnectedHandler(const QString& service) {
    m_connected = false;
    emit connectedChanged();
}

void BackendDictsWithArraysClient::propertiesChangedHandler(QString iface, QVariantMap changes, QStringList) {
    if (iface != "com.yarpc.backend.dictsWithArrays") {
        return;
    }
    if (changes.contains("DictArrayProperty")) {
        emit dictArrayPropertyChanged();
    }
}

DictsArrayMethodPendingCall* BackendDictsWithArraysClient::DictsArrayMethod(
    QVariant numbers
) {
    QMap<QString, QList<QMap<QString, uint>>> arg_0;
    arg_0 = numbers.value<QMap<QString, QList<QMap<QString, uint>>>>();

    return DictsArrayMethod(
        arg_0
    );
}
DictsArrayMethodPendingCall* BackendDictsWithArraysClient::DictsArrayMethod(
    QMap<QString, QList<QMap<QString, uint>>> numbers
) {
    QDBusArgument dbusnumbers;
    dbusnumbers << numbers;
    QDBusInterface iface(
        "com.yarpc.backend",
        "/com/yarpc/backend/dicts",
        "com.yarpc.backend.dictsWithArrays",
        QDBusConnection::sessionBus()
    );
    QDBusPendingCall pendingCall {iface.asyncCall(
        "DictsArrayMethod",
        QVariant::fromValue(dbusnumbers)
    )};
    return new DictsArrayMethodPendingCall(pendingCall, this);
}

DictsArrayMethodPendingCall::DictsArrayMethodPendingCall(QDBusPendingCall pendingCall, QObject *parent)
: QObject(parent), m_watcher(pendingCall, this) {
    QObject::connect(
        &m_watcher, &QDBusPendingCallWatcher::finished,
        this, &DictsArrayMethodPendingCall::callFinished
    );
}

void DictsArrayMethodPendingCall::callFinished(QDBusPendingCallWatcher *watcher)
{
    QDBusPendingReply<QMap<QString, QList<QMap<QString, uint>>>> reply {*watcher};
    if (!reply.isValid()) {
        emit error(reply.error());
    } else {
        emit finished(reply);
    }
    deleteLater();
}


void BackendDictsWithArraysClient::DictsArraySignalDBusHandler(QDBusMessage content) {
    QMap<QString, QList<QMap<QString, uint>>> arg_0;
    content.arguments()[0].value<QDBusArgument>() >> arg_0;
    emit dictsArraySignalReceived(
        QVariant::fromValue(arg_0)
    );
}


QMap<QString, QList<QMap<QString, uint>>> BackendDictsWithArraysClient::getDictArrayProperty() const {
    QDBusInterface iface(
        "com.yarpc.backend",
        "/com/yarpc/backend/dicts",
        "org.freedesktop.DBus.Properties",
        QDBusConnection::sessionBus()
    );
    QDBusReply<QDBusVariant> reply = iface.call(
        "Get",
        "com.yarpc.backend.dictsWithArrays",
        "DictArrayProperty"
    );
    QMap<QString, QList<QMap<QString, uint>>> unmarshalled{};
    if (reply.isValid()) {
        auto marshalled = qvariant_cast<QDBusArgument>(reply.value().variant());
        marshalled >> unmarshalled;
    }
    return unmarshalled;
}


QVariant BackendDictsWithArraysClient::getVariantDictArrayProperty() const {
    auto unmarshalled = getDictArrayProperty();
    QVariant marshalled;
    marshalled = QVariant::fromValue(unmarshalled);

    return marshalled;
}


void BackendDictsWithArraysClient::setDictArrayProperty(const QMap<QString, QList<QMap<QString, uint>>> &newValue) {
    QDBusInterface iface(
        "com.yarpc.backend",
        "/com/yarpc/backend/dicts",
        "org.freedesktop.DBus.Properties",
        QDBusConnection::sessionBus()
    );
    QDBusArgument marshalled;
    QDBusVariant v;
    v.setVariant(QVariant::fromValue(newValue));
    marshalled << v;
    iface.call(
        "Set",
        "com.yarpc.backend.dictsWithArrays",
        "DictArrayProperty",
        QVariant::fromValue<QDBusArgument>(marshalled)
    );
}

void BackendDictsWithArraysClient::setVariantDictArrayProperty(QVariant value ) {
    QMap<QString, QList<QMap<QString, uint>>> unmarshalled;
    unmarshalled = value.value<QMap<QString, QList<QMap<QString, uint>>>>();

    setDictArrayProperty(unmarshalled);
}
