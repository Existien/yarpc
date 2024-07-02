/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/02.1_with_args.yml
 *   Object: WithArgs
 *   Template: qt6/service_source.j2
 */
#include "WithArgsInterface.hpp"
#include "WithArgsInterfaceAdaptor.hpp"
#include "Connection.hpp"
#include "types.hpp"

using namespace gen::with_args;

WithArgsInterface::WithArgsInterface(QObject* parent)
: QObject(parent) {
    registerMetaTypes();
    QObject::connect(
        &Connection::instance(),
        &Connection::connectedChanged,
        this,
        &WithArgsInterface::connectedChanged
    );
    QObject::connect(
        &Connection::instance(),
        &Connection::registrationChanged,
        this,
        &WithArgsInterface::connectedChanged
    );
}

void WithArgsInterface::connect() {
    Connection::instance().registerWithArgs(this);
}

void WithArgsInterface::disconnect() {
    Connection::instance().unregisterWithArgs();
}

void WithArgsInterface::finishCall(const QDBusMessage &reply)
{
    Connection::instance().send(reply);
}

bool WithArgsInterface::getConnected() const {
    return (
        Connection::instance().getConnected()
        && Connection::instance().isWithArgsRegistered()
    );
}

void WithArgsInterface::EmitNotified(
    QString message
) {
    if (Connection::instance().WithArgs() != nullptr ) {
        emit Connection::instance().WithArgs()->Notified(
            message
        );
    }
}

void WithArgsInterface::EmitNotified(
    QVariant message
) {
    QString arg_0;
    arg_0 = message.value<QString>();

    EmitNotified(
        arg_0
    );
}

void WithArgsInterface::EmitOrderReceived(
    QString item,
    uint amount,
    double pricePerItem
) {
    if (Connection::instance().WithArgs() != nullptr ) {
        emit Connection::instance().WithArgs()->OrderReceived(
            item,
            amount,
            pricePerItem
        );
    }
}

void WithArgsInterface::EmitOrderReceived(
    QVariant item,
    QVariant amount,
    QVariant pricePerItem
) {
    QString arg_0;
    arg_0 = item.value<QString>();

    uint arg_1;
    arg_1 = amount.value<uint>();

    double arg_2;
    arg_2 = pricePerItem.value<double>();

    EmitOrderReceived(
        arg_0,
        arg_1,
        arg_2
    );
}

NotifyPendingReply::NotifyPendingReply(QDBusMessage call, QObject *parent) : QObject(parent) {
    m_call = call;
    m_args = NotifyArgs{
        .message = m_call.arguments()[0].value<QString>(),
    };
}

NotifyArgs NotifyPendingReply::args() {
    return m_args;
}


void NotifyPendingReply::sendReply(
) {
    auto dbusReply = m_call.createReply();
    auto iface = dynamic_cast<WithArgsInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(dbusReply);
    }
    deleteLater();
}

void NotifyPendingReply::sendError(const QString& name, const QString& message) {
    auto error_reply = m_call.createErrorReply(name, message);
    auto iface = dynamic_cast<WithArgsInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(error_reply);
    }
    deleteLater();
}

void NotifyPendingReply::sendError(const DBusError &error) {
    auto error_reply = m_call.createErrorReply(error);
    auto iface = dynamic_cast<WithArgsInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(error_reply);
    }
    deleteLater();
}

void WithArgsInterface::handleNotifyCalled(QDBusMessage call) {
    auto reply = new NotifyPendingReply(call, this);
    emit notifyCalled(reply);
}

OrderPendingReply::OrderPendingReply(QDBusMessage call, QObject *parent) : QObject(parent) {
    m_call = call;
    m_args = OrderArgs{
        .item = m_call.arguments()[0].value<QString>(),
        .amount = m_call.arguments()[1].value<uint>(),
        .pricePerItem = m_call.arguments()[2].value<double>(),
    };
}

OrderArgs OrderPendingReply::args() {
    return m_args;
}

void OrderPendingReply::sendReply(
    QVariant reply
) {
    double unmarshalled;
    unmarshalled = reply.value<double>();

    sendReply(unmarshalled);
}

void OrderPendingReply::sendReply(
    const double &reply
) {
    auto dbusReply = m_call.createReply(QVariant::fromValue(reply));
    auto iface = dynamic_cast<WithArgsInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(dbusReply);
    }
    deleteLater();
}

void OrderPendingReply::sendError(const QString& name, const QString& message) {
    auto error_reply = m_call.createErrorReply(name, message);
    auto iface = dynamic_cast<WithArgsInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(error_reply);
    }
    deleteLater();
}

void OrderPendingReply::sendError(const DBusError &error) {
    auto error_reply = m_call.createErrorReply(error);
    auto iface = dynamic_cast<WithArgsInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(error_reply);
    }
    deleteLater();
}

void WithArgsInterface::handleOrderCalled(QDBusMessage call) {
    auto reply = new OrderPendingReply(call, this);
    emit orderCalled(reply);
}

double WithArgsInterface::getSpeed() const {
    return m_Speed;
}

void WithArgsInterface::setSpeed(const double &value ) {
    m_Speed = value;
    emit speedChanged();
    if (Connection::instance().WithArgs() != nullptr ) {
        QVariantMap changedProps;
        changedProps.insert("Speed", QVariant::fromValue(value));
        emitPropertiesChangedSignal(changedProps);
    }
}

QVariant WithArgsInterface::getVariantSpeed() const {
    auto unmarshalled = getSpeed();
    QVariant marshalled;
    marshalled = QVariant::fromValue(unmarshalled);

    return marshalled;
}

void WithArgsInterface::setVariantSpeed(QVariant value ) {
    double unmarshalled;
    unmarshalled = value.value<double>();

    setSpeed(unmarshalled);
}

uint WithArgsInterface::getDistance() const {
    return m_Distance;
}

void WithArgsInterface::setDistance(const uint &value ) {
    m_Distance = value;
    emit distanceChanged();
    if (Connection::instance().WithArgs() != nullptr ) {
        QVariantMap changedProps;
        changedProps.insert("Distance", QVariant::fromValue(value));
        emitPropertiesChangedSignal(changedProps);
    }
}

QVariant WithArgsInterface::getVariantDistance() const {
    auto unmarshalled = getDistance();
    QVariant marshalled;
    marshalled = QVariant::fromValue(unmarshalled);

    return marshalled;
}

void WithArgsInterface::setVariantDistance(QVariant value ) {
    uint unmarshalled;
    unmarshalled = value.value<uint>();

    setDistance(unmarshalled);
}

double WithArgsInterface::getDuration() const {
    return m_Duration;
}

void WithArgsInterface::setDuration(const double &value ) {
    m_Duration = value;
    emit durationChanged();
    if (Connection::instance().WithArgs() != nullptr ) {
        QVariantMap changedProps;
        changedProps.insert("Duration", QVariant::fromValue(value));
        emitPropertiesChangedSignal(changedProps);
    }
}

QVariant WithArgsInterface::getVariantDuration() const {
    auto unmarshalled = getDuration();
    QVariant marshalled;
    marshalled = QVariant::fromValue(unmarshalled);

    return marshalled;
}

void WithArgsInterface::setVariantDuration(QVariant value ) {
    double unmarshalled;
    unmarshalled = value.value<double>();

    setDuration(unmarshalled);
}


void WithArgsInterface::emitPropertiesChangedSignal(const QVariantMap &changedProps) {
    auto signal = QDBusMessage::createSignal(
        "/com/yarpc/testservice/withArgs",
        "org.freedesktop.DBus.Properties",
        "PropertiesChanged"
    );
    signal << "com.yarpc.testservice.withArgs";
    signal << changedProps;
    signal << QStringList{};
    Connection::instance().send(signal);
}