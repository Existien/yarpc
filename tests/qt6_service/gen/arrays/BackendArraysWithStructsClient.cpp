/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/04.2_arrays_with_structs.yml
 *   Object: ArraysWithStructs
 *   Template: qt6/client_source.j2
 */
#include "BackendArraysWithStructsClient.hpp"
#include "types.hpp"
#include <QDBusConnection>
#include <QDBusInterface>
#include <QDBusReply>
#include <QDBusPendingCall>
#include <QDBusPendingReply>


using namespace gen::arrays;
using namespace BackendArraysWithStructsClientUtils;

BackendArraysWithStructsClient::BackendArraysWithStructsClient(QObject* parent)
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
        "/com/yarpc/backend/arrays",
        "com.yarpc.backend.arraysWithStructs",
        QDBusConnection::sessionBus()
    );
    m_connected = iface.isValid();

    connect(
        &m_watcher, &QDBusServiceWatcher::serviceRegistered,
        this, &BackendArraysWithStructsClient::connectedHandler
    );
    connect(
        &m_watcher, &QDBusServiceWatcher::serviceUnregistered,
        this, &BackendArraysWithStructsClient::disconnectedHandler
    );

    QDBusConnection::sessionBus().connect(
        "com.yarpc.backend",
        "/com/yarpc/backend/arrays",
        "org.freedesktop.DBus.Properties",
        "PropertiesChanged",
        this,
        SLOT(propertiesChangedHandler(QString, QVariantMap, QStringList))
    );
    QDBusConnection::sessionBus().connect(
        "com.yarpc.backend",
        "/com/yarpc/backend/arrays",
        "com.yarpc.backend.arraysWithStructs",
        "ArrayStructSignal",
        this,
        SLOT(ArrayStructSignalDBusHandler(QDBusMessage))
    );

}

bool BackendArraysWithStructsClient::getConnected() const {
    return m_connected;
}

QVariantMap BackendArraysWithStructsClient::getAllProperties() const {
    QDBusInterface iface(
        "com.yarpc.backend",
        "/com/yarpc/backend/arrays",
        "org.freedesktop.DBus.Properties",
        QDBusConnection::sessionBus()
    );
    QDBusReply<QVariantMap> reply = iface.call(
        "GetAll",
        "com.yarpc.backend.arraysWithStructs"
    );
    if (!reply.isValid()) {
        return QVariantMap();
    } else {
        return reply.value();
    }
}

void BackendArraysWithStructsClient::connectedHandler(const QString& service) {
    m_connected = true;
    emit connectedChanged();
}

void BackendArraysWithStructsClient::disconnectedHandler(const QString& service) {
    m_connected = false;
    emit connectedChanged();
}

void BackendArraysWithStructsClient::propertiesChangedHandler(QString iface, QVariantMap changes, QStringList) {
    if (iface != "com.yarpc.backend.arraysWithStructs") {
        return;
    }
    if (changes.contains("ArrayStructProperty")) {
        emit arrayStructPropertyChanged();
    }
}

ArrayStructMethodPendingCall* BackendArraysWithStructsClient::ArrayStructMethod(
    QVariant numbers
) {
    QList<StructArray> arg_0;
    for (auto& item_0 : numbers.value<QVariantList>()) {
        StructArray o_0;
        o_0 = item_0.value<StructArray>();

        arg_0.push_back(o_0);
    }

    return ArrayStructMethod(
        arg_0
    );
}
ArrayStructMethodPendingCall* BackendArraysWithStructsClient::ArrayStructMethod(
    QList<StructArray> numbers
) {
    QDBusArgument dbusnumbers;
    dbusnumbers << numbers;
    QDBusInterface iface(
        "com.yarpc.backend",
        "/com/yarpc/backend/arrays",
        "com.yarpc.backend.arraysWithStructs",
        QDBusConnection::sessionBus()
    );
    QDBusPendingCall pendingCall {iface.asyncCall(
        "ArrayStructMethod",
        QVariant::fromValue(dbusnumbers)
    )};
    return new ArrayStructMethodPendingCall(pendingCall, this);
}

ArrayStructMethodPendingCall::ArrayStructMethodPendingCall(QDBusPendingCall pendingCall, QObject *parent)
: QObject(parent), m_watcher(pendingCall, this) {
    QObject::connect(
        &m_watcher, &QDBusPendingCallWatcher::finished,
        this, &ArrayStructMethodPendingCall::callFinished
    );
}

void ArrayStructMethodPendingCall::callFinished(QDBusPendingCallWatcher *watcher)
{
    QDBusPendingReply<QList<SimonsArray>> reply {*watcher};
    if (!reply.isValid()) {
        emit error(reply.error());
    } else {
        QList<SimonsArray> finishedReply = reply;
        emit finished(finishedReply);
    }
    deleteLater();
}


void BackendArraysWithStructsClient::ArrayStructSignalDBusHandler(QDBusMessage content) {
    QList<StructArray> arg_0;
    content.arguments()[0].value<QDBusArgument>() >> arg_0;
    emit arrayStructSignalReceived(
        QVariant::fromValue(arg_0)
    );
}


QList<StructArray> BackendArraysWithStructsClient::getArrayStructProperty() const {
    QDBusInterface iface(
        "com.yarpc.backend",
        "/com/yarpc/backend/arrays",
        "org.freedesktop.DBus.Properties",
        QDBusConnection::sessionBus()
    );
    QDBusReply<QDBusVariant> reply = iface.call(
        "Get",
        "com.yarpc.backend.arraysWithStructs",
        "ArrayStructProperty"
    );
    QList<StructArray> unmarshalled{};
    if (reply.isValid()) {
        auto marshalled = qvariant_cast<QDBusArgument>(reply.value().variant());
        marshalled >> unmarshalled;
    }
    return unmarshalled;
}


QVariant BackendArraysWithStructsClient::getVariantArrayStructProperty() const {
    auto unmarshalled = getArrayStructProperty();
    QVariant marshalled;
    QList<QVariant> list_0;
    for (auto& item_0 : unmarshalled) {
        QVariant o_0;
        o_0 = QVariant::fromValue(item_0);

        list_0.push_back(o_0);
    }
    marshalled = QVariant::fromValue(list_0);

    return marshalled;
}


void BackendArraysWithStructsClient::setArrayStructProperty(const QList<StructArray> &newValue) {
    QDBusInterface iface(
        "com.yarpc.backend",
        "/com/yarpc/backend/arrays",
        "org.freedesktop.DBus.Properties",
        QDBusConnection::sessionBus()
    );
    QDBusArgument marshalled;
    QDBusVariant v;
    v.setVariant(QVariant::fromValue(newValue));
    marshalled << v;
    iface.call(
        "Set",
        "com.yarpc.backend.arraysWithStructs",
        "ArrayStructProperty",
        QVariant::fromValue<QDBusArgument>(marshalled)
    );
}

void BackendArraysWithStructsClient::setVariantArrayStructProperty(QVariant value ) {
    QList<StructArray> unmarshalled;
    for (auto& item_0 : value.value<QVariantList>()) {
        StructArray o_0;
        o_0 = item_0.value<StructArray>();

        unmarshalled.push_back(o_0);
    }

    setArrayStructProperty(unmarshalled);
}
