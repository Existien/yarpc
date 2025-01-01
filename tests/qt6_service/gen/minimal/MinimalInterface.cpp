/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/01_minimal.yml
 *   Object: Minimal
 *   Template: qt6/service_source.j2
 */
#include <QDBusArgument>
#include "MinimalInterface.hpp"
#include "MinimalInterfaceAdaptor.hpp"
#include "Connection.hpp"
#include "types.hpp"

using namespace gen::minimal;

MinimalInterface::MinimalInterface(QObject* parent)
: QObject(parent) {
    registerMetaTypes();
    QObject::connect(
        &Connection::instance(),
        &Connection::connectedChanged,
        this,
        &MinimalInterface::connectedChanged
    );
    QObject::connect(
        &Connection::instance(),
        &Connection::registrationChanged,
        this,
        &MinimalInterface::connectedChanged
    );
}

void MinimalInterface::connect() {
    Connection::instance().registerMinimal(this);
}

void MinimalInterface::disconnect() {
    Connection::instance().unregisterMinimal();
}

void MinimalInterface::finishCall(const QDBusMessage &reply)
{
    Connection::instance().send(reply);
}

bool MinimalInterface::getConnected() const {
    return (
        Connection::instance().getConnected()
        && Connection::instance().isMinimalRegistered()
    );
}

void MinimalInterface::EmitBumped(
) {
    if (Connection::instance().Minimal() != nullptr ) {
        emit Connection::instance().Minimal()->Bumped(

        );
    }
}


BumpPendingReply::BumpPendingReply(QDBusMessage call, QObject *parent) : QObject(parent) {
    m_call = call;
    m_args = BumpArgs{
    };
}

BumpArgs BumpPendingReply::args() {
    return m_args;
}


void BumpPendingReply::sendReply(
) {
    auto dbusReply = m_call.createReply();
    auto iface = dynamic_cast<MinimalInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(dbusReply);
    }
    deleteLater();
}

void BumpPendingReply::sendError(const QString& name, const QString& message) {
    auto error_reply = m_call.createErrorReply(name, message);
    auto iface = dynamic_cast<MinimalInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(error_reply);
    }
    deleteLater();
}

void BumpPendingReply::sendError(const DBusError &error) {
    auto error_reply = m_call.createErrorReply(error);
    auto iface = dynamic_cast<MinimalInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(error_reply);
    }
    deleteLater();
}

void MinimalInterface::handleBumpCalled(QDBusMessage call) {
    auto reply = new BumpPendingReply(call, this);
    emit bumpCalled(reply);
}


void MinimalInterface::emitPropertiesChangedSignal(const QVariantMap &changedProps) {
    auto signal = QDBusMessage::createSignal(
        "/com/yarpc/testservice/minimal",
        "org.freedesktop.DBus.Properties",
        "PropertiesChanged"
    );
    signal << "com.yarpc.testservice.minimal";
    signal << changedProps;
    signal << QStringList{};
    Connection::instance().send(signal);
}