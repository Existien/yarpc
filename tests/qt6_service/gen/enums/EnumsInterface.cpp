/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/06.1_enums.yml
 *   Object: Enums
 *   Template: qt6/service_source.j2
 */
#include <QDBusArgument>
#include "EnumsInterface.hpp"
#include "EnumsInterfaceAdaptor.hpp"
#include "Connection.hpp"
#include "types.hpp"

using namespace gen::enums;

EnumsInterface::EnumsInterface(QObject* parent)
: QObject(parent) {
    registerMetaTypes();
    QObject::connect(
        &Connection::instance(),
        &Connection::connectedChanged,
        this,
        &EnumsInterface::connectedChanged
    );
    QObject::connect(
        &Connection::instance(),
        &Connection::registrationChanged,
        this,
        &EnumsInterface::connectedChanged
    );
}

void EnumsInterface::connect() {
    Connection::instance().registerEnums(this);
}

void EnumsInterface::disconnect() {
    Connection::instance().unregisterEnums();
}

void EnumsInterface::finishCall(const QDBusMessage &reply)
{
    Connection::instance().send(reply);
}

bool EnumsInterface::getConnected() const {
    return (
        Connection::instance().getConnected()
        && Connection::instance().isEnumsRegistered()
    );
}

EnumMethodPendingReply::EnumMethodPendingReply(QDBusMessage call, QObject *parent) : QObject(parent) {
    m_call = call;
    m_args = EnumMethodArgs{
        .color = m_call.arguments()[0].value<Color::Type>(),
    };
}

EnumMethodArgs EnumMethodPendingReply::args() {
    return m_args;
}

void EnumMethodPendingReply::sendReply(
    QVariant reply
) {
    Color::Type unmarshalled;
    unmarshalled = reply.value<Color::Type>();

    sendReply(unmarshalled);
}

void EnumMethodPendingReply::sendReply(
    const Color::Type &reply
) {
    auto replyToSend = static_cast<int>(reply);
    auto dbusReply = m_call.createReply(QVariant::fromValue(replyToSend));
    auto iface = dynamic_cast<EnumsInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(dbusReply);
    }
    deleteLater();
}

void EnumMethodPendingReply::sendError(const QString& name, const QString& message) {
    auto error_reply = m_call.createErrorReply(name, message);
    auto iface = dynamic_cast<EnumsInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(error_reply);
    }
    deleteLater();
}

void EnumMethodPendingReply::sendError(const DBusError &error) {
    auto error_reply = m_call.createErrorReply(error);
    auto iface = dynamic_cast<EnumsInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(error_reply);
    }
    deleteLater();
}

void EnumsInterface::handleEnumMethodCalled(QDBusMessage call) {
    auto reply = new EnumMethodPendingReply(call, this);
    emit enumMethodCalled(reply);
}

void EnumsInterface::EmitEnumSignal(
    Color::Type color
) {
    if (Connection::instance().Enums() != nullptr ) {
        emit Connection::instance().Enums()->EnumSignal(
            color
        );
    }
}

void EnumsInterface::EmitEnumSignal(
    QVariant color
) {
    Color::Type arg_0;
    arg_0 = color.value<Color::Type>();

    EmitEnumSignal(
        arg_0
    );
}

Color::Type EnumsInterface::getEnumProperty() const {
    return m_EnumProperty;
}

void EnumsInterface::setEnumProperty(const Color::Type &value ) {
    m_EnumProperty = value;
    emit enumPropertyChanged();
    if (Connection::instance().Enums() != nullptr ) {
        QVariantMap changedProps;
        changedProps.insert("EnumProperty", QVariant::fromValue(static_cast<int>(value)));
        emitPropertiesChangedSignal(changedProps);
    }
}

QVariant EnumsInterface::getVariantEnumProperty() const {
    auto unmarshalled = getEnumProperty();
    QVariant marshalled;
    marshalled = QVariant::fromValue(unmarshalled);

    return marshalled;
}

void EnumsInterface::setVariantEnumProperty(QVariant value ) {
    Color::Type unmarshalled;
    unmarshalled = value.value<Color::Type>();

    setEnumProperty(unmarshalled);
}


void EnumsInterface::emitPropertiesChangedSignal(const QVariantMap &changedProps) {
    auto signal = QDBusMessage::createSignal(
        "/com/yarpc/testservice/enums",
        "org.freedesktop.DBus.Properties",
        "PropertiesChanged"
    );
    signal << "com.yarpc.testservice.enums";
    signal << changedProps;
    signal << QStringList{};
    Connection::instance().send(signal);
}