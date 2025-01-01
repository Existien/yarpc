/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/04.2_arrays_with_structs.yml
 *   Object: ArraysWithStructs
 *   Template: qt6/service_source.j2
 */
#include <QDBusArgument>
#include "ArraysWithStructsInterface.hpp"
#include "ArraysWithStructsInterfaceAdaptor.hpp"
#include "Connection.hpp"
#include "types.hpp"

using namespace gen::arrays;

ArraysWithStructsInterface::ArraysWithStructsInterface(QObject* parent)
: QObject(parent) {
    registerMetaTypes();
    QObject::connect(
        &Connection::instance(),
        &Connection::connectedChanged,
        this,
        &ArraysWithStructsInterface::connectedChanged
    );
    QObject::connect(
        &Connection::instance(),
        &Connection::registrationChanged,
        this,
        &ArraysWithStructsInterface::connectedChanged
    );
}

void ArraysWithStructsInterface::connect() {
    Connection::instance().registerArraysWithStructs(this);
}

void ArraysWithStructsInterface::disconnect() {
    Connection::instance().unregisterArraysWithStructs();
}

void ArraysWithStructsInterface::finishCall(const QDBusMessage &reply)
{
    Connection::instance().send(reply);
}

bool ArraysWithStructsInterface::getConnected() const {
    return (
        Connection::instance().getConnected()
        && Connection::instance().isArraysWithStructsRegistered()
    );
}

ArrayStructMethodPendingReply::ArrayStructMethodPendingReply(QDBusMessage call, QObject *parent) : QObject(parent) {
    m_call = call;
    QList<StructArray> arg_0;
    {
        auto marshalled = m_call.arguments()[0].value<QDBusArgument>();
        marshalled >> arg_0;
    }
    m_args = ArrayStructMethodArgs{
        .numbers = arg_0,
    };
}

ArrayStructMethodArgs ArrayStructMethodPendingReply::args() {
    return m_args;
}

void ArrayStructMethodPendingReply::sendReply(
    QVariant reply
) {
    QList<SimonsArray> unmarshalled;
    for (auto& item_0 : reply.value<QVariantList>()) {
        SimonsArray o_0;
        o_0 = item_0.value<SimonsArray>();

        unmarshalled.push_back(o_0);
    }

    sendReply(unmarshalled);
}

void ArrayStructMethodPendingReply::sendReply(
    const QList<SimonsArray> &reply
) {
    auto dbusReply = m_call.createReply(QVariant::fromValue(reply));
    auto iface = dynamic_cast<ArraysWithStructsInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(dbusReply);
    }
    deleteLater();
}

void ArrayStructMethodPendingReply::sendError(const QString& name, const QString& message) {
    auto error_reply = m_call.createErrorReply(name, message);
    auto iface = dynamic_cast<ArraysWithStructsInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(error_reply);
    }
    deleteLater();
}

void ArrayStructMethodPendingReply::sendError(const DBusError &error) {
    auto error_reply = m_call.createErrorReply(error);
    auto iface = dynamic_cast<ArraysWithStructsInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(error_reply);
    }
    deleteLater();
}

void ArraysWithStructsInterface::handleArrayStructMethodCalled(QDBusMessage call) {
    auto reply = new ArrayStructMethodPendingReply(call, this);
    emit arrayStructMethodCalled(reply);
}

void ArraysWithStructsInterface::EmitArrayStructSignal(
    QList<StructArray> numbers
) {
    if (Connection::instance().ArraysWithStructs() != nullptr ) {
        emit Connection::instance().ArraysWithStructs()->ArrayStructSignal(
            numbers
        );
    }
}

void ArraysWithStructsInterface::EmitArrayStructSignal(
    QVariant numbers
) {
    QList<StructArray> arg_0;
    for (auto& item_0 : numbers.value<QVariantList>()) {
        StructArray o_0;
        o_0 = item_0.value<StructArray>();

        arg_0.push_back(o_0);
    }

    EmitArrayStructSignal(
        arg_0
    );
}

QList<StructArray> ArraysWithStructsInterface::getArrayStructProperty() const {
    return m_ArrayStructProperty;
}

void ArraysWithStructsInterface::setArrayStructProperty(const QList<StructArray> &value ) {
    m_ArrayStructProperty = value;
    emit arrayStructPropertyChanged();
    if (Connection::instance().ArraysWithStructs() != nullptr ) {
        QVariantMap changedProps;
        changedProps.insert("ArrayStructProperty", QVariant::fromValue(value));
        emitPropertiesChangedSignal(changedProps);
    }
}

QVariant ArraysWithStructsInterface::getVariantArrayStructProperty() const {
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

void ArraysWithStructsInterface::setVariantArrayStructProperty(QVariant value ) {
    QList<StructArray> unmarshalled;
    for (auto& item_0 : value.value<QVariantList>()) {
        StructArray o_0;
        o_0 = item_0.value<StructArray>();

        unmarshalled.push_back(o_0);
    }

    setArrayStructProperty(unmarshalled);
}


void ArraysWithStructsInterface::emitPropertiesChangedSignal(const QVariantMap &changedProps) {
    auto signal = QDBusMessage::createSignal(
        "/com/yarpc/testservice/arrays",
        "org.freedesktop.DBus.Properties",
        "PropertiesChanged"
    );
    signal << "com.yarpc.testservice.arraysWithStructs";
    signal << changedProps;
    signal << QStringList{};
    Connection::instance().send(signal);
}