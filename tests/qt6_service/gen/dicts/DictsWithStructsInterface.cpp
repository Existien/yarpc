/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/05.2_dictionaries_with_structs.yml
 *   Object: DictsWithStructs
 *   Template: qt6/service_source.j2
 */
#include "DictsWithStructsInterface.hpp"
#include "DictsWithStructsInterfaceAdaptor.hpp"
#include "Connection.hpp"

using namespace gen::dicts;

DictsWithStructsInterface::DictsWithStructsInterface(QObject* parent)
: QObject(parent) {
    QObject::connect(
        &Connection::instance(),
        &Connection::connectedChanged,
        this,
        &DictsWithStructsInterface::connectedChanged
    );
    QObject::connect(
        &Connection::instance(),
        &Connection::registrationChanged,
        this,
        &DictsWithStructsInterface::connectedChanged
    );
}

void DictsWithStructsInterface::connect() {
    Connection::instance().registerDictsWithStructs(this);
}

void DictsWithStructsInterface::disconnect() {
    Connection::instance().unregisterDictsWithStructs();
}

void DictsWithStructsInterface::finishCall(const QDBusMessage &reply)
{
    Connection::instance().send(reply);
}

bool DictsWithStructsInterface::getConnected() const {
    return (
        Connection::instance().getConnected()
        && Connection::instance().isDictsWithStructsRegistered()
    );
}

DictsStructMethodPendingReply::DictsStructMethodPendingReply(QDBusMessage call, QObject *parent) : QObject(parent) {
    m_call = call;
    m_args = DictsStructMethodArgs{
        .numbers = m_call.arguments()[0].value<QMap<$1, $2>>(),
    };
}

DictsStructMethodArgs DictsStructMethodPendingReply::args() {
    return m_args;
}

void DictsStructMethodPendingReply::sendReply(
    const QMap<$1, $2> &reply
) {
    auto dbusReply = m_call.createReply();
    dbusReply << reply;
    auto iface = dynamic_cast<DictsWithStructsInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(dbusReply);
    }
    deleteLater();
}

void DictsStructMethodPendingReply::sendError(const QString& name, const QString& message) {
    auto error_reply = m_call.createErrorReply(name, message);
    auto iface = dynamic_cast<DictsWithStructsInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(error_reply);
    }
    deleteLater();
}

void DictsStructMethodPendingReply::sendError(const DBusError &error) {
    auto error_reply = m_call.createErrorReply(error);
    auto iface = dynamic_cast<DictsWithStructsInterface*>(parent());
    if (iface != nullptr) {
        iface->finishCall(error_reply);
    }
    deleteLater();
}

void DictsWithStructsInterface::handleDictsStructMethodCalled(QDBusMessage call) {
    auto reply = new DictsStructMethodPendingReply(call, this);
    emit dictsStructMethodCalled(reply);
}

void DictsWithStructsInterface::EmitDictStructSignal(
    QMap<$1, $2> numbers
) {
    if (Connection::instance().DictsWithStructs() != nullptr ) {
        emit Connection::instance().DictsWithStructs()->DictStructSignal(
            numbers
        );
    }
}

QMap<$1, $2> DictsWithStructsInterface::getDictStructProperty() const {
    return m_DictStructProperty;
}

void DictsWithStructsInterface::setDictStructProperty(const QMap<$1, $2> &value ) {
    m_DictStructProperty = value;
    emit dictStructPropertyChanged();
    if (Connection::instance().DictsWithStructs() != nullptr ) {
        QVariantMap changedProps;
        changedProps.insert("DictStructProperty", value);
        emitPropertiesChangedSignal(changedProps);
    }
}


void DictsWithStructsInterface::emitPropertiesChangedSignal(const QVariantMap &changedProps) {
    auto signal = QDBusMessage::createSignal(
        "/com/yarpc/testservice/dicts",
        "org.freedesktop.DBus.Properties",
        "PropertiesChanged"
    );
    signal << "com.yarpc.testservice.dictsWithStructs";
    signal << changedProps;
    signal << QStringList{};
    Connection::instance().send(signal);
}