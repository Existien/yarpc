/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/06.3_enums_with_dicts.yml
 *   Object: EnumsWithDicts
 *   Template: qt6/client_source.j2
 */
#include "BackendEnumsWithDictsClient.hpp"
#include "types.hpp"
#include <QDBusConnection>
#include <QDBusInterface>
#include <QDBusReply>
#include <QDBusPendingCall>
#include <QDBusPendingReply>


using namespace gen::enums;
using namespace BackendEnumsWithDictsClientUtils;

BackendEnumsWithDictsClient::BackendEnumsWithDictsClient(QObject* parent)
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
    QVariant color
) {
    QMap<Color::Type, Color::Type> arg_0;
    arg_0 = color.value<QMap<Color::Type, Color::Type>>();

    return EnumMethod(
        arg_0
    );
}
EnumMethodPendingCall* BackendEnumsWithDictsClient::EnumMethod(
    QMap<Color::Type, Color::Type> color
) {
    QDBusArgument dbuscolor;
    dbuscolor << *reinterpret_cast<const QMap<int, int>*>(&color);
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
    QDBusPendingReply<QMap<int, int>> reply {*watcher};
    if (!reply.isValid()) {
        emit error(reply.error());
    } else {
        QMap<int, int> finishedReply = reply;
        emit finished(*reinterpret_cast<const QMap<Color::Type, Color::Type>*>(&finishedReply));
    }
    deleteLater();
}


void BackendEnumsWithDictsClient::EnumSignalDBusHandler(QDBusMessage content) {
    QMap<Color::Type, Color::Type> arg_0;
    content.arguments()[0].value<QDBusArgument>() >> arg_0;
    emit enumSignalReceived(
        QVariant::fromValue(arg_0)
    );
}


QMap<Color::Type, Color::Type> BackendEnumsWithDictsClient::getEnumProperty() const {
    QDBusInterface iface(
        "com.yarpc.backend",
        "/com/yarpc/backend/enums",
        "org.freedesktop.DBus.Properties",
        QDBusConnection::sessionBus()
    );
    QDBusReply<QDBusVariant> reply = iface.call(
        "Get",
        "com.yarpc.backend.enumsWithDicts",
        "EnumProperty"
    );
    QMap<Color::Type, Color::Type> unmarshalled{};
    if (reply.isValid()) {
        auto marshalled = qvariant_cast<QDBusArgument>(reply.value().variant());
        marshalled >> unmarshalled;
    }
    return unmarshalled;
}


QVariant BackendEnumsWithDictsClient::getVariantEnumProperty() const {
    auto unmarshalled = getEnumProperty();
    QVariant marshalled;
    marshalled = QVariant::fromValue(unmarshalled);

    return marshalled;
}


void BackendEnumsWithDictsClient::setEnumProperty(const QMap<Color::Type, Color::Type> &newValue) {
    QDBusInterface iface(
        "com.yarpc.backend",
        "/com/yarpc/backend/enums",
        "org.freedesktop.DBus.Properties",
        QDBusConnection::sessionBus()
    );
    QDBusArgument marshalled;
    QDBusVariant v;
    v.setVariant(QVariant::fromValue(*reinterpret_cast<const QMap<int, int>*>(&newValue)));
    marshalled << v;
    iface.call(
        "Set",
        "com.yarpc.backend.enumsWithDicts",
        "EnumProperty",
        QVariant::fromValue<QDBusArgument>(marshalled)
    );
}

void BackendEnumsWithDictsClient::setVariantEnumProperty(QVariant value ) {
    QMap<Color::Type, Color::Type> unmarshalled;
    unmarshalled = value.value<QMap<Color::Type, Color::Type>>();

    setEnumProperty(unmarshalled);
}
