/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/06.2_enums_with_arrays.yml
 *   Object: EnumsWithArrays
 *   Template: qt6/service_source.j2
 */
#include <QDBusArgument>
#include "EnumsWithArraysInterface.hpp"
#include "EnumsWithArraysInterfaceAdaptor.hpp"
#include "Connection.hpp"
#include "types.hpp"

using namespace gen::enums;

EnumsWithArraysInterface::EnumsWithArraysInterface(QObject* parent)
: QObject(parent) {
    registerMetaTypes();
    QObject::connect(
        &Connection::instance(),
        &Connection::connectedChanged,
        this,
        &EnumsWithArraysInterface::connectedChanged
    );
    QObject::connect(
        &Connection::instance(),
        &Connection::registrationChanged,
        this,
        &EnumsWithArraysInterface::connectedChanged
    );
}

void EnumsWithArraysInterface::connect() {
    Connection::instance().registerEnumsWithArrays(this);
}

void EnumsWithArraysInterface::disconnect() {
    Connection::instance().unregisterEnumsWithArrays();
}

void EnumsWithArraysInterface::finishCall(const QDBusMessage &reply)
{
    Connection::instance().send(reply);
}

bool EnumsWithArraysInterface::getConnected() const {
    return (
        Connection::instance().getConnected()
        && Connection::instance().isEnumsWithArraysRegistered()
    );
}

EnumMethodPendingReply::EnumMethodPendingReply(QDBusMessage call, QObject *parent) : QObject(parent) {
    m_call = call;
    QList<> arg_0;
    {
        auto marshalled = m_call.arguments()[0].value<QDBusArgument>();
        marshalled >> arg_0;
    }
    m_args = EnumMethodArgs{
        .color = arg_0,
    };
}

EnumMethodArgs EnumMethodPendingReply::args() {
    return m_args;
}

void EnumMethodPendingReply::sendReply(
    QVariant reply
) {
    QList<> unmarshalled;
    for (auto& item_0 : reply.value<QVariantList>()) {
         o_0;
        o_0 = item_0.value<>();

        unmarshalled.push_back(o_0);
    }

    sendReply(unmarshalled);
}

void EnumMethodPendingReply::sendReply(
    const QList<> &reply
) {
    auto dbusReply = m_call.createReply(QVariant::fromValue(reply));
    auto iface = dynamic_cast<EnumsWithArraysInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(dbusReply);
    }
    deleteLater();
}

void EnumMethodPendingReply::sendError(const QString& name, const QString& message) {
    auto error_reply = m_call.createErrorReply(name, message);
    auto iface = dynamic_cast<EnumsWithArraysInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(error_reply);
    }
    deleteLater();
}

void EnumMethodPendingReply::sendError(const DBusError &error) {
    auto error_reply = m_call.createErrorReply(error);
    auto iface = dynamic_cast<EnumsWithArraysInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(error_reply);
    }
    deleteLater();
}

void EnumsWithArraysInterface::handleEnumMethodCalled(QDBusMessage call) {
    auto reply = new EnumMethodPendingReply(call, this);
    emit enumMethodCalled(reply);
}

void EnumsWithArraysInterface::EmitEnumSignal(
    QList<> color
) {
    if (Connection::instance().EnumsWithArrays() != nullptr ) {
        emit Connection::instance().EnumsWithArrays()->EnumSignal(
            color
        );
    }
}

void EnumsWithArraysInterface::EmitEnumSignal(
    QVariant color
) {
    QList<> arg_0;
    for (auto& item_0 : color.value<QVariantList>()) {
         o_0;
        o_0 = item_0.value<>();

        arg_0.push_back(o_0);
    }

    EmitEnumSignal(
        arg_0
    );
}

QList<> EnumsWithArraysInterface::getEnumProperty() const {
    return m_EnumProperty;
}

void EnumsWithArraysInterface::setEnumProperty(const QList<> &value ) {
    m_EnumProperty = value;
    emit enumPropertyChanged();
    if (Connection::instance().EnumsWithArrays() != nullptr ) {
        QVariantMap changedProps;
        changedProps.insert("EnumProperty", QVariant::fromValue(value));
        emitPropertiesChangedSignal(changedProps);
    }
}

QVariant EnumsWithArraysInterface::getVariantEnumProperty() const {
    auto unmarshalled = getEnumProperty();
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

void EnumsWithArraysInterface::setVariantEnumProperty(QVariant value ) {
    QList<> unmarshalled;
    for (auto& item_0 : value.value<QVariantList>()) {
         o_0;
        o_0 = item_0.value<>();

        unmarshalled.push_back(o_0);
    }

    setEnumProperty(unmarshalled);
}


void EnumsWithArraysInterface::emitPropertiesChangedSignal(const QVariantMap &changedProps) {
    auto signal = QDBusMessage::createSignal(
        "/com/yarpc/testservice/enums",
        "org.freedesktop.DBus.Properties",
        "PropertiesChanged"
    );
    signal << "com.yarpc.testservice.enumsWithArrays";
    signal << changedProps;
    signal << QStringList{};
    Connection::instance().send(signal);
}